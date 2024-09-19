from fastapi import FastAPI , Body


app = FastAPI()

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
def school(mustafe: dict = Body(...)):
    print(mustafe)
    return{
        "new_post": f"school: {mustafe['school']}, establish: {mustafe['establish']}"
    }