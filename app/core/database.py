from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# silnik bazy danych
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} # tylko dla sqlite
)

# fabryka sesji - każde zapytanie dostanie swoją sesję
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Klasa bazowa dla modeli
Base = declarative_base()

# Dependency do używania w endpointach - automatyczne zarządzanie sesją
def get_db():
    db = SessionLocal() # tworzymy sesję
    try:
        yield db # oddajemy sesję do użycia
    finally:
        db.close() # zamykamy sesję

