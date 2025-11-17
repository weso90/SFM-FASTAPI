from passlib.context import CryptContext

# kontekst do hashowania
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashuje hasło
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Sprawdza czy hasło jest poprawne
    """
    return pwd_context.verify(plain_password, hashed_password)