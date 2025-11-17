from pydantic import BaseModel, EmailStr
from datetime import datetime

# Dane wejściowe - rejestracja
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

# Dane wyjściowe - odpowiedź API (bez hasła)
class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True # pozwala konwertować SQLALchemy model -> Pydantic