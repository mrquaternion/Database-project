from config import engine, SessionLocal
from models import Base, CoupeDuMonde

# Drop and create tables. Use with caution
Base.metadata.drop_all(bind=engine)  
Base.metadata.create_all(bind=engine)


