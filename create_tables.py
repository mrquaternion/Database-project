from config import engine, SessionLocal
from models import Base, CoupeDuMonde

Base.metadata.drop_all(bind=engine)  
Base.metadata.create_all(bind=engine)

db = SessionLocal()
coupes = db.query(CoupeDuMonde).all()
print(coupes)
db.close()
