import os
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models import create_db_and_tables
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


app = FastAPI()

Oauth_scheme = OAuth2PasswordBearer(tokenUrl="auth/login-form")
becrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")




from auth_router import auth_router

app.include_router(auth_router)

@app.on_event("startup")
async def startup():
    create_db_and_tables()





