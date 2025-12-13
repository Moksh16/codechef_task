from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError,jwt
from passlib.context import CryptContext
app = FastAPI()


secret_key = "92670e7408350f15c914a49baa1fff522fd89a97c370b8aafdaa74735f66cb87"
algorithm = "HS256"
access_token_expires_minutes = 30

db= {
    "moksh":{
        'username':"Moksh",
        'Full Name': "Moksh Shah",
        'email': "Moksh@gmail.com",
        'hashed_password':"",
        'disabled':False
    }
}

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    username: str | None = None
class User(BaseModel):
    username:str
    email: str | None=None
    full_name: str | None=None
    disabled: bool | None=None

class UserInDB(BaseModel):
    hashed_password: str

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db,username:str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)
def authenticate_user(db, username:str, password:str):
    user = get_user(db,username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
# class Data(BaseModel):
#     name:str

# @app.post('/create/')
# def create(data:Data):
#     return {"Data":data}

# @app.get('/test/{item_id}')
# def inside(item_id:str, query:int=1):
#     return {"Hello":item_id}