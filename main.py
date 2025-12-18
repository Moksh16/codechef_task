from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError,jwt
from passlib.context import CryptContext
from fastapi.params import Body
from random import randrange


oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="Login")
password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Post(BaseModel):
    argument: str
    evidence: str

app = FastAPI()
submissions= []


def find_index_post(id):
    for i,p in enumerate(submissions):
        if p["id"] ==id:
            return i

@app.post('/auth/signup')
def register(username):
    return {"message": f"{username}, you are registered"}


@app.post('/case/submit')
def add_argument(post: Post):
    my_post = post.dict()
    my_post["key"] = randrange(0,1000000)
    submissions.append(my_post)
    return {"Message":"Argument and evidence received" }

@app.get('/case/all')
def get_submissions():
    return submissions

app.delete('/case/delete/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    index = find_index_post(id)
    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    submissions.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
