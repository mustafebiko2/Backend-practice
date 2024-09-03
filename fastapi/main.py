from fastapi import FastAPI

app = FastAPI()
#get - get an information
#post - create something
#put - update something already exist
#delet - delet something

@app.get("/")
async def root():
    return {"message": "Hello World"}



