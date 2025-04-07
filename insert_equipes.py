from sqlalchemy.orm import Session
from models import CoupeDuMonde, Equipe
from config import SessionLocal

equipes_par_edition = {
    "1986": ["Argentine", "Allemagne", "France", "Brésil", "Angleterre", "Mexique", "Italie", "Espagne", "URSS", "Danemark"],
    "1990": ["Allemagne", "Argentine", "Italie", "Angleterre", "Brésil", "Espagne", "Pays-Bas", "Cameroun", "Tchécoslovaquie", "Suède"],
    "1994": ["Brésil", "Italie", "Suède", "Bulgarie", "Allemagne", "Pays-Bas", "Roumanie", "Espagne", "Argentine", "Mexique"],
    "1998": ["France", "Brésil", "Croatie", "Pays-Bas", "Italie", "Allemagne", "Argentine", "Mexique", "Nigéria", "Espagne"],
    "2002": ["Brésil", "Allemagne", "Turquie", "Corée du Sud", "Espagne", "Angleterre", "Italie", "Sénégal", "Etats-Unis", "Japon"],
    "2006": ["Italie", "France", "Allemagne", "Portugal", "Brésil", "Argentine", "Angleterre", "Ukraine", "Espagne", "Mexique"],
    "2010": ["Espagne", "Pays-Bas", "Allemagne", "Uruguay", "Brésil", "Argentine", "Ghana", "Paraguay", "Japon", "Portugal"],
    "2014": ["Allemagne", "Argentine", "Pays-Bas", "Brésil", "Colombie", "France", "Belgique", "Costa Rica", "Chili", "Mexique"],
    "2018": ["France", "Croatie", "Belgique", "Angleterre", "Brésil", "Uruguay", "Russie", "Suède", "Colombie", "Mexique"],
    "2022": ["Argentine", "France", "Croatie", "Maroc", "Angleterre", "Brésil", "Portugal", "Pays-Bas", "Japon", "Sénégal"]
}


def insert_equipes(db):
    db: Session = SessionLocal()
    try:
        for edition, equipes in equipes_par_edition.items():
            coupe = db.query(CoupeDuMonde).filter(CoupeDuMonde.edition == edition).first()
            if coupe:
                for nom_pays in equipes:
                    equipe = Equipe(nom_pays=nom_pays, coupe_du_monde_id=coupe.id)
                    db.add(equipe)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Erreur insertion:", e)
    finally:
        db.close()

if __name__ == "__main__":
    insert_equipes()
