from sqlalchemy.orm import Session
from models import CoupeDuMonde
from config import SessionLocal  

coupes_du_monde = [
    {"edition": "1986", "pays_hote": "Mexique", "nombre_equipes": 24, "vainqueur": "Argentine"},
    {"edition": "1990", "pays_hote": "Italie", "nombre_equipes": 24, "vainqueur": "Allemagne de l'Ouest"},
    {"edition": "1994", "pays_hote": "États-Unis", "nombre_equipes": 24, "vainqueur": "Brésil"},
    {"edition": "1998", "pays_hote": "France", "nombre_equipes": 32, "vainqueur": "France"},
    {"edition": "2002", "pays_hote": "Corée du Sud / Japon", "nombre_equipes": 32, "vainqueur": "Brésil"},
    {"edition": "2006", "pays_hote": "Allemagne", "nombre_equipes": 32, "vainqueur": "Italie"},
    {"edition": "2010", "pays_hote": "Afrique du Sud", "nombre_equipes": 32, "vainqueur": "Espagne"},
    {"edition": "2014", "pays_hote": "Brésil", "nombre_equipes": 32, "vainqueur": "Allemagne"},
    {"edition": "2018", "pays_hote": "Russie", "nombre_equipes": 32, "vainqueur": "France"},
    {"edition": "2022", "pays_hote": "Qatar", "nombre_equipes": 32, "vainqueur": "Argentine"},
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
