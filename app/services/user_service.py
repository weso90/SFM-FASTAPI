from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: Session, user_data: UserCreate) -> User:
    """
    Tworzy nowego użytkownika
    """
    # hashuj hasło
    hashed_password = hash_password(user_data.password)

    # utwórz obiekt User
    db_user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password
    )

    #zapisz do bazy
    db.add(db_user)
    db.commit()
    db.refresh(db_user) #odśwież żeby mieć id i created_at

    return db_user

def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Pobiera użytkownika po emailu
    """
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> User | None:
    """
    Pobiera użytkownika po username
    """
    return db.query(User). filter(User.username == username).first()
