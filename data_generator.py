from sqlalchemy.orm import Session
from faker import Faker
from config import SessionLocal
from models import Joueur, Personnel, Partie, Arbitre, ArbitreDans, Stade, Equipe, CoupeDuMonde
from insert_cdm import insert_coupes_du_monde
from insert_equipes import insert_equipes
from collections import defaultdict
import random
from datetime import date

fake = Faker()

def generate_parties(db: Session, n):
    phases = ["Phase de groupes", "Huitièmes de finale", "Quarts de finale", "Demi-finale", "Finale"]
    
    equipes = db.query(Equipe).all()
    stades = db.query(Stade).all()

    if len(equipes) < 2 or len(stades) == 0:
        return
    
    equipes_par_edition = defaultdict(list)

    for equipe in equipes:
        if equipe.coupe:
            edition = equipe.coupe.annee
            equipes_par_edition[edition].append(equipe)
    
    for _ in range(n):
        edition = random.choice(list(equipes_par_edition.keys()))
        equipes_edition = equipes_par_edition[edition]

        if len(equipes_edition) < 2:
            continue

        equipe1, equipe2 = random.sample(equipes_edition, 2)
        stade = random.choice(stades)
        phase = random.choice(phases)

        try:
            year_int = int(edition)
        except ValueError:
            year_int = 2022

        date_partie = fake.date_between_dates(
            date_start=date(year_int, 6, 1),
            date_end=date(year_int, 7, 31)
        )

        partie = Partie(
            date_partie=date_partie,
            phase=phase,
            stade_id=stade.id_stade,
            equipe_dom_id=equipe1.id_equipe,
            equipe_ext_id=equipe2.id_equipe,
            score_dom=fake.random_int(min=0, max=5),
            score_ext=fake.random_int(min=0, max=5),
            coupe_id=equipe1.coupe_id
        )
        db.add(partie)

    db.commit()

def generate_stades(db: Session, n):
    type_de_stades = ["Stadium", "Arena", "Park", "Field"]
    for _ in range(n):
        name = fake.company()
        type_de_stade = fake.random_element(type_de_stades)
        stade = Stade(
            nom=f"{name} {type_de_stade}",
            ville=fake.city(),
            pays=fake.country()
        )
        db.add(stade)
    db.commit()

def generate_joueurs(db: Session, n):
    equipes = db.query(Equipe).all()
    for equipe in equipes:
        for _ in range(n): 
            joueur = Joueur(
                nom=fake.last_name(),
                prenom=fake.first_name_male(),
                date_naissance=fake.date_of_birth(minimum_age=18, maximum_age=40),
                numero=fake.random_int(min=1, max=99),
                position=fake.random_element(elements=["Gardien", "Défenseur", "Milieu", "Attaquant"]),
                cartons_jaunes=fake.random_int(min=0, max=3),
                cartons_rouges=fake.random_int(min=0, max=1),
                equipe_id=equipe.id_equipe
            )
            db.add(joueur)
    db.commit()

def generate_personnel(db: Session):
    equipes = db.query(Equipe).all()
    for equipe in equipes:
        for role in ["Entraîneur", "Adjoint"]:
            staff = Personnel(
                nom=fake.last_name(),
                prenom=fake.first_name_male(),
                date_naissance=fake.date_of_birth(minimum_age=30, maximum_age=65),
                role_principal=role,
                equipe_id=equipe.id_equipe
            )
            db.add(staff)
    db.commit()

def generate_arbitres(db: Session, n):
    nationalities = ["Français", "Espagnol", "Italien", "Allemand", "Anglais"]
    
    for _ in range(n):
        arbitre = Arbitre(
            nom=fake.last_name(),
            prenom=fake.first_name_male(),
            date_naissance=fake.date_of_birth(minimum_age=30, maximum_age=50),
            nationalite=fake.random_element(nationalities)
        )
        db.add(arbitre)
    db.commit()

def generate_arbitres_dans(db: Session):
    parties = db.query(Partie).all()
    arbitres = db.query(Arbitre).all()
    roles = ["Arbitre principal", "Arbitre assistant", "Quatrième arbitre"]
    
    if not arbitres or not parties:
        return  

    for partie in parties:
        arbitres_sel = random.sample(arbitres, k=min(4, len(arbitres)))
        
        for i, arbitre in enumerate(arbitres_sel):
            role = roles[i % len(roles)]
            arbitre_dans = ArbitreDans(
                arbitre_id=arbitre.id_arbitre,
                partie_id=partie.id_partie,
                role_arbitre=role
            )
            db.add(arbitre_dans)

    db.commit()

def main():
    db = SessionLocal()

    insert_coupes_du_monde(db)
    insert_equipes(db)
    # Generate 10 stades
    generate_stades(db, n=10)
    # Generate 11 players for each team
    generate_joueurs(db, n=11)
    generate_personnel(db)
    generate_parties(db, n=100)
    generate_arbitres(db, n=20)
    generate_arbitres_dans(db)

    db.close()

if __name__ == "__main__":
    main()
