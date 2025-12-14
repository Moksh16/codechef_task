from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError,jwt
from passlib.context import CryptContext
from fastapi.params import Body

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="Login")
password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Post(BaseModel):
    argument: str
    evidence: str


secret_key = "897fd83ed4066efcbcdabd0d204e20897b3966555d421916581435833ef6c9c2"
algorithm = "HS256"
app = FastAPI()
submissions= {}
@app.post('/auth/register')
def register(username):
    return {"message": f"{username}, you are registered"}


@app.post('/argument')
def add_argument(post: Post):
    return {"Message":"Argument received" }

@app.get('/submission')
def get_submissions():
    return submissions

