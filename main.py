from fastapi import FastAPI
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from auth_router import auth_router
from models import create_db_and_tables


app = FastAPI()



Oauth_scheme = OAuth2PasswordBearer(tokenUrl="auth")


app.include_router(auth_router)

@app.on_event("startup")
async def startup():
    create_db_and_tables()





