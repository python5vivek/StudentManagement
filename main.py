from fastapi import FastAPI
from uvicorn import run
from pydantic import BaseModel
import json

Data = {}
idcount = 0
app = FastAPI()

def save():
    global Data
    open("data.json","w").write(json.dumps(Data))

def load():
    global Data,idcount
    Data = json.loads(open("data.json","r").read())
    for id in Data:
        idcount = int(id)
load()

class studentDetail(BaseModel):
    Name:str
    Age:int
    Class:str
    Height:float

@app.get("/")
def homepage():
    return Data

@app.post("/register")
def register(data:studentDetail):
    global idcount
    Data[f"{idcount}"] = {"Name":data.Name,"Age":data.Age,"Class":"7th","Height":167.5}
    idcount += 1
    save()
    return data.json()

@app.delete("/delete/{id}")
def delete(id):
    if id in Data:
        del Data[id]
        save()
        return {"msg":"Successfull"}
    else:
        return {"error":404}



run(app,port=8000)