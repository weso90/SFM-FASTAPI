from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import User
from app.api.v1 import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Family Manager")

#podłącz router
app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "API działa"}