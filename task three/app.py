from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Num(BaseModel):
    number_1: int
    number_2: int

@app.get('/')
async def read_root():
    return {"message": "Привет, отпарвь POST на /calculate/"}

@app.post('/calculate/')
async def calculate_result(numb: Num):
    return {
        "num_1": numb.number_1,
        "num_2": numb.number_2,
        "result": numb.number_1 + numb.number_2
    }
