from symtable import Class
from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Field, Session
from pydantic import EmailStr

class UserBase(SQLModel):
    name: str = Field(index=True)
    email: EmailStr = Field(index=True)
    password: str = Field(index=True)

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = { "check_same_thread": False }
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session,Depends(get_session)]








