from config import engine, SessionLocal
from models import Base, CoupeDuMonde

# Crée les tables si elles n'existent pas encore
Base.metadata.create_all(bind=engine)

# Test simple
db = SessionLocal()
coupes = db.query(CoupeDuMonde).all()
print(coupes)
db.close()
