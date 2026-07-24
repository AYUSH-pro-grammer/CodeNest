from database.connection import Base, engine
from database import models


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("database ready")
    
    