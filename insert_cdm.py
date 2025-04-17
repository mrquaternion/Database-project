from sqlalchemy.orm import Session
from models import CoupeDuMonde
from config import SessionLocal  

coupes_du_monde = [
    {"annee": "1986", "pays_hote": "Mexique", "nb_equipes": 24, "vainqueur": "Argentine"},
    {"annee": "1990", "pays_hote": "Italie", "nb_equipes": 24, "vainqueur": "Allemagne de l'Ouest"},
    {"annee": "1994", "pays_hote": "États-Unis", "nb_equipes": 24, "vainqueur": "Brésil"},
    {"annee": "1998", "pays_hote": "France", "nb_equipes": 32, "vainqueur": "France"},
    {"annee": "2002", "pays_hote": "Corée du Sud / Japon", "nb_equipes": 32, "vainqueur": "Brésil"},
    {"annee": "2006", "pays_hote": "Allemagne", "nb_equipes": 32, "vainqueur": "Italie"},
    {"annee": "2010", "pays_hote": "Afrique du Sud", "nb_equipes": 32, "vainqueur": "Espagne"},
    {"annee": "2014", "pays_hote": "Brésil", "nb_equipes": 32, "vainqueur": "Allemagne"},
    {"annee": "2018", "pays_hote": "Russie", "nb_equipes": 32, "vainqueur": "France"},
    {"annee": "2022", "pays_hote": "Qatar", "nb_equipes": 32, "vainqueur": "Argentine"},
]

def insert_coupes_du_monde(db):
    db: Session = SessionLocal()
    for data in coupes_du_monde:
        coupe = CoupeDuMonde(**data)
        db.add(coupe)
    db.commit()
    db.close()

if __name__ == "__main__":
    insert_coupes_du_monde()
