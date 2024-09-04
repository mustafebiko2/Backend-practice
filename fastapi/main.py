from fastapi import FastAPI
from typing import Optional

app = FastAPI()
#get - get an information
#post - create something
#put - update something already exist
#delet - delet something

@app.get('/greet/{name}')
async def greet_name(name:str, age:int):
   return{"message": F"hello, {name}", "age": age}


