from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


#root path
@app.post("/")
def root(item:dict=Body(...)):
    print(item)
    return {"item":item}