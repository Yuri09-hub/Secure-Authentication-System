from pydantic import EmailStr
from fastapi import APIRouter, HTTPException, Depends
from models import SessionDep, User, UserBase
from jose import jwt
from main import SECRET_KEY,ALGORITHM, becrypt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(tags=["auth"],prefix="/auth")



def creat_token(id, duration_token =timedelta(minutes=30)):
    date_expiretaion = datetime.now(timezone.utc) + duration_token
    dict_info = {"sub": str(id), "exp":int(date_expiretaion.timestamp())}
    jwt_token = jwt.encode(dict_info, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token



def user_autenticate(email,password,session:SessionDep):
    user = session.get(User,email)
    if not user:
        return False
    elif not becrypt.verify(password,user.password):
        return False
    else:
        return user



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

@auth_router.post("/login-form")
async def login_form(session: SessionDep, form_data:OAuth2PasswordRequestForm = Depends()):
    user = user_autenticate(form_data.password,form_data.username,session)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist or invalid credentials")
    else:
        access_token = creat_token(user.id)
        return {
            "access_token":access_token,
            "token_type":"bearer",
        }