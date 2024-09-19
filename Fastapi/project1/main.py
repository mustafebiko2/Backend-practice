from fastapi import FastAPI , Body
from pydantic import BaseModel



app = FastAPI()

class post(BaseModel):
    school: str
    establish: int

@app.get('/home')
def home():
    return{"message":"this is home "}

from fastapi import FastAPI, Body

app = FastAPI()

@app.post('/createpost')
def create_post(payload: dict = Body(...)):
    print(payload)
    return {
        "new_post": f"name: {payload['name']}, phone: {payload['phone']}, email: {payload['email']}"
    }

@app.post('/school')
def school(new_post: post):
    print(new_post)
    return{"data": "new post"}
    