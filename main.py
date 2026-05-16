from fastapi import FastAPI, Depends
from fastapi.security import  OAuth2PasswordBearer
from models import create_db_and_tables, User
from dotenv import load_dotenv
from passlib.context import CryptContext
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


app = FastAPI()



becrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

Oauth_scheme = OAuth2PasswordBearer(tokenUrl="auth/login-form")


from auth_router import auth_router, get_current_user

app.include_router(auth_router)

@app.on_event("startup")
async def startup():
    create_db_and_tables()

@app.get("/me")
async def readme(user:User = Depends(get_current_user)):
    return user




