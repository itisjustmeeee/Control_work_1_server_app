from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

message_bd = []

@app.get('/')
async def get_messages():
    return message_bd

@app.post('/feedback')
async def get_message(mes: Feedback):
    message_bd.append({"name": mes.name, "message": mes.message})
    return {"message": f"Feedback received. Thank you, {mes.name}"}

# запускать через /docs в feedback try out для добавления ответа, в / try out для просмотра всех ответов