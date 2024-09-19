from fastapi import FastAPI , Body


app = FastAPI()

@app.get('/home')
def home():
    return{"message":"this is home "}

@app.post('/createpost')
def create_post(payload: dict = Body(...)):
    print(payload)
    return{"message":"post has been created"}