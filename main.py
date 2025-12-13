from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError,jwt
from passlib.context import CryptContext

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="Login")
password_haser = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()

@app.post('/auth/register')
def register(username):
    return {"username": username}



