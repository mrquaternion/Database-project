from typing import List, Optional 
from sqlalchemy import ForeignKey, String, Date 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date

class Base(DeclarativeBase):
    pass

class CoupeDuMonde(Base):
    __tablename__ = "coupe_du_monde"

    id: Mapped[int] = mapped_column(primary_key=True)
    edition: Mapped[str] = mapped_column(String(50), nullable=False)
    pays_hote: Mapped[str] = mapped_column(String(50), nullable=False)
    nombre_equipes: Mapped[int] = mapped_column(nullable=False)
    vainqueur: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    # Relation avec les équipes
    equipes: Mapped[List["Equipe"]] = relationship(back_populates="coupe_du_monde")

class Equipe(Base):
    __tablename__ = "equipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom_pays: Mapped[str] = mapped_column(String(50), nullable=False)
    coupe_du_monde_id: Mapped[int] = mapped_column(ForeignKey("coupe_du_monde.id"))
    coupe_du_monde: Mapped["CoupeDuMonde"] = relationship(back_populates="equipes")

    # Relation avec les joueurs et le personnel
    joueurs: Mapped[List["Joueur"]] = relationship(back_populates="equipe")
    personnels: Mapped[List["Personnel"]] = relationship(back_populates="equipe")

    # Relation avec les parties
    parties_reveceur: Mapped[List["Partie"]] = relationship("Partie", foreign_keys="[Partie.equipe_receveuse_id]", back_populates="equipe_receveuse")
    parties_visiteur: Mapped[List["Partie"]] = relationship("Partie", foreign_keys="[Partie.equipe_visiteuse_id]", back_populates="equipe_visiteuse")


class Joueur(Base):
    __tablename__ = "joueur"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    prenom: Mapped[str] = mapped_column(String(50), nullable=False)
    date_naissance: Mapped[date] = mapped_column(Date, nullable=False)
    numero: Mapped[int] = mapped_column(nullable=False)
    position: Mapped[str] = mapped_column(String(50), nullable=False)
    carton_jaune: Mapped[int] = mapped_column(default=0, nullable=False)
    carton_rouge: Mapped[int] = mapped_column(default=0, nullable=False)

    # Relation avec l'équipe
    equipe_id: Mapped[int] = mapped_column(ForeignKey("equipe.id"))
    equipe: Mapped["Equipe"] = relationship(back_populates="joueurs")

class Personnel(Base):
    __tablename__ = "personnel"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    prenom: Mapped[str] = mapped_column(String(50), nullable=False)
    date_naissance: Mapped[date] = mapped_column(Date, nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relation avec l'équipe
    equipe_id: Mapped[int] = mapped_column(ForeignKey("equipe.id"))
    equipe: Mapped["Equipe"] = relationship(back_populates="personnels")

class Stade(Base):
    __tablename__ = "stade"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    ville: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relation avec les parties
    parties: Mapped[List["Partie"]] = relationship(back_populates="stade")

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Partie(Base):
    __tablename__ = "partie"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(Date)
    phase: Mapped[str] = mapped_column(String(50), nullable=False)

    stade_id: Mapped[int] = mapped_column(ForeignKey("stade.id"))
    stade: Mapped["Stade"] = relationship(back_populates="parties")

    # Relation avec les équipes
    equipe_receveuse_id: Mapped[int] = mapped_column(ForeignKey("equipe.id"))
    equipe_visiteuse_id: Mapped[int] = mapped_column(ForeignKey("equipe.id"))

    equipe_receveuse: Mapped["Equipe"] = relationship("Equipe", foreign_keys=[equipe_receveuse_id], back_populates="parties_reveceur")
    equipe_visiteuse: Mapped["Equipe"] = relationship("Equipe", foreign_keys=[equipe_visiteuse_id], back_populates="parties_visiteur")

    score_receveur: Mapped[int] = mapped_column(Integer, nullable=True)
    score_visiteuse: Mapped[int] = mapped_column(Integer, nullable=True)
    # Relation avec les arbitres
    arbitres: Mapped[List["ArbitreDans"]] = relationship("ArbitreDans", back_populates="partie")

class Arbitre(Base):
    __tablename__ = "arbitre"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    prenom: Mapped[str] = mapped_column(String(50), nullable=False)
    date_naissance: Mapped[date] = mapped_column(Date, nullable=False)
    nationalite: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relation avec les parties
    parties: Mapped[List["ArbitreDans"]] = relationship("ArbitreDans",back_populates="arbitre")

class ArbitreDans(Base):
    __tablename__ = "arbitre_dans"

    partie_id: Mapped[int] = mapped_column(ForeignKey("partie.id"), primary_key=True)
    arbitre_id: Mapped[int] = mapped_column(ForeignKey("arbitre.id"), primary_key=True)

    role: Mapped[str] = mapped_column(String(20), nullable=False)

    # Relation avec les parties et les arbitres
    partie: Mapped["Partie"] = relationship("Partie", back_populates="arbitres")
    arbitre: Mapped["Arbitre"] = relationship("Arbitre", back_populates="parties")
