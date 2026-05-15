from fastapi import APIRouter
from models import SessionDep, User, UserBase
from passlib.context import CryptContext

becrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


auth_router = APIRouter(tags=["auth"],prefix="/auth")

@auth_router.post("/Creat_account",response_model=User)
async def Creat_account(user: UserBase, session: SessionDep):

    user_form = User(
        name= user.name,
        email= user.email,
        password= becrypt.encrypt(user.password),
    )
    session.add(user_form)
    session.commit()
    session.refresh(user_form)

    return user_form

@auth_router.post("/login")
async def login():
    ...