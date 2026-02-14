from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post('/user')
async def age_check(user: User):
    x = False
    if (user.age >= 18):
        x = True
    return {
            "name": user.name,
            "age": user.age,
            "is_adult": x
        }

# запускать через /docs в try out