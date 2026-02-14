from fastapi import FastAPI
from models import User

app = FastAPI()

new_user = User (
    name="Гузаирова Ольга",
    Id = 6
)

@app.get('/users')
async def get_user():
    return new_user

# чтобы посмотреть, надо перейти в /users