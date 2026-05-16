from sqlmodel import select
from fastapi import APIRouter, HTTPException, Depends
from models import SessionDep, User, UserBase
from jose import jwt
from main import SECRET_KEY,ALGORITHM, becrypt, Oauth_scheme
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(tags=["auth"],prefix="/auth")



def creat_token(id, duration_token =timedelta(minutes=30)):
    date_expiretaion = datetime.now(timezone.utc) + duration_token
    dict_info = {"sub": str(id), "exp":int(date_expiretaion.timestamp())}
    jwt_token = jwt.encode(dict_info, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token

def get_current_user(session:SessionDep,token: str = Depends(Oauth_scheme)):
    verify = jwt.decode(token,SECRET_KEY,ALGORITHM)

    user_id = verify.get("sub")

    user = session.get(User,user_id)

    return user



def user_autenticate(email,password, session:SessionDep):
    user = select(User).where(User.email == email)
    users = session.exec(user).first()
    if not users:
        return False
    elif not becrypt.verify(password,users.password):
        return False

    return users



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
async def login_form(
        session: SessionDep,
        form_data:OAuth2PasswordRequestForm = Depends()):

    user = user_autenticate(form_data.username,form_data.password,session)
    if not user:
        print("não esta a achar o objeto")
        raise HTTPException(status_code=404, detail="não esta a achar o objeto")

    access_token = creat_token(user.id)
    return {
            "access_token":access_token,
            "token_type":"bearer",
        }

