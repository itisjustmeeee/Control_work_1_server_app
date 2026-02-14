from fastapi import FastAPI
from models import User

app = FastAPI()

current_user = User(
    name = "Гузаирова Ольга",
    Id = 6
)

@app.get('/users')
async def get_user():
    return current_user

@app.get('/')
async def root():
    return {"message": "Сервер работает."}

# чтобы посмотреть данные пользователя, надо перейти в /users