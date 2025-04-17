from typing import List, Optional
from sqlalchemy import ForeignKey, String, Date, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date

class Base(DeclarativeBase):
    pass

class CoupeDuMonde(Base):
    __tablename__ = "coupe_du_monde"

    id_cdm: Mapped[int] = mapped_column(primary_key=True)
    annee: Mapped[int] = mapped_column(nullable=False, unique=True)
    pays_hote: Mapped[str] = mapped_column(String(100), nullable=False)
    nb_equipes: Mapped[int] = mapped_column(nullable=False)
    vainqueur: Mapped[str] = mapped_column(String(100), nullable=False)

    equipes: Mapped[List["Equipe"]] = relationship(back_populates="coupe")

class Equipe(Base):
    __tablename__ = "equipe"

    id_equipe: Mapped[int] = mapped_column(primary_key=True)
    coupe_id: Mapped[int] = mapped_column(ForeignKey("coupe_du_monde.id_cdm"))
    nom_pays: Mapped[str] = mapped_column(String(100), nullable=False)
    nb_joueurs: Mapped[int] = mapped_column(nullable=False) 

    coupe: Mapped["CoupeDuMonde"] = relationship(back_populates="equipes")
    joueurs: Mapped[List["Joueur"]] = relationship(back_populates="equipe")
    personnels: Mapped[List["Personnel"]] = relationship(back_populates="equipe")

    parties_receveur: Mapped[List["Partie"]] = relationship(
        "Partie", foreign_keys="[Partie.equipe_dom_id]", back_populates="equipe_receveur")
    parties_visiteur: Mapped[List["Partie"]] = relationship(
        "Partie", foreign_keys="[Partie.equipe_ext_id]", back_populates="equipe_visiteur")

class Joueur(Base):
    __tablename__ = "joueur"

    id_joueur: Mapped[int] = mapped_column(primary_key=True)
    equipe_id: Mapped[int] = mapped_column(ForeignKey("equipe.id_equipe"))
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)
    date_naissance: Mapped[date] = mapped_column(Date, nullable=False)
    annee_deces: Mapped[Optional[int]] = mapped_column(nullable=True)
    numero: Mapped[int] = mapped_column(nullable=False)
    position: Mapped[str] = mapped_column(String(50), nullable=False)
    cartons_jaunes: Mapped[int] = mapped_column(default=0, nullable=False)
    cartons_rouges: Mapped[int] = mapped_column(default=0, nullable=False)

    equipe: Mapped["Equipe"] = relationship(back_populates="joueurs")

class Personnel(Base):
    __tablename__ = "personnel"

    id_personnel: Mapped[int] = mapped_column(primary_key=True)
    equipe_id: Mapped[int] = mapped_column(ForeignKey("equipe.id_equipe"))
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)
    date_naissance: Mapped[date] = mapped_column(Date, nullable=False)
    annee_deces: Mapped[Optional[int]] = mapped_column(nullable=True)
    role_principal: Mapped[str] = mapped_column(String(50), nullable=False)

    equipe: Mapped["Equipe"] = relationship(back_populates="personnels")

class Stade(Base):
    __tablename__ = "stade"

    id_stade: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    pays: Mapped[str] = mapped_column(String(100), nullable=False)
    ville: Mapped[str] = mapped_column(String(100), nullable=False)

    parties: Mapped[List["Partie"]] = relationship(back_populates="stade")

class Partie(Base):
    __tablename__ = "partie"

    id_partie: Mapped[int] = mapped_column(primary_key=True)
    coupe_id: Mapped[int] = mapped_column(ForeignKey("coupe_du_monde.id_cdm"))
    date_partie: Mapped[date] = mapped_column(Date, nullable=False)
    phase: Mapped[str] = mapped_column(String(50), nullable=False)
    stade_id: Mapped[int] = mapped_column(ForeignKey("stade.id_stade"))

    equipe_dom_id: Mapped[int] = mapped_column(ForeignKey("equipe.id_equipe"))
    equipe_ext_id: Mapped[int] = mapped_column(ForeignKey("equipe.id_equipe"))
    score_dom: Mapped[int] = mapped_column(nullable=False)
    score_ext: Mapped[int] = mapped_column(nullable=False)

    stade: Mapped["Stade"] = relationship(back_populates="parties")
    equipe_receveur: Mapped["Equipe"] = relationship(
        "Equipe", foreign_keys=[equipe_dom_id], back_populates="parties_receveur")
    equipe_visiteur: Mapped["Equipe"] = relationship(
        "Equipe", foreign_keys=[equipe_ext_id], back_populates="parties_visiteur")

    arbitres: Mapped[List["ArbitreDans"]] = relationship(back_populates="partie")

class Arbitre(Base):
    __tablename__ = "arbitre"

    id_arbitre: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)
    date_naissance: Mapped[date] = mapped_column(Date, nullable=False)
    annee_deces: Mapped[Optional[int]] = mapped_column(nullable=True)
    nationalite: Mapped[str] = mapped_column(String(50), nullable=False)

    parties: Mapped[List["ArbitreDans"]] = relationship(back_populates="arbitre")

class ArbitreDans(Base):
    __tablename__ = "arbitre_dans"

    partie_id: Mapped[int] = mapped_column(ForeignKey("partie.id_partie"), primary_key=True)
    arbitre_id: Mapped[int] = mapped_column(ForeignKey("arbitre.id_arbitre"), primary_key=True)
    role_arbitre: Mapped[str] = mapped_column(String(50), nullable=False)

    partie: Mapped["Partie"] = relationship(back_populates="arbitres")
    arbitre: Mapped["Arbitre"] = relationship(back_populates="parties")
