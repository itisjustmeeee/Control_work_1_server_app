from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

banned_words = {
    "кринж", "кринжа", "кринжу", "кринжем", "кринжами", "кринже",
    "кринжи", "кринжов", "кринжам", "кринжах",
    
    "рофл", "рофла", "рофлу", "рофлом", "рофлами", "рофле",
    "рофлы", "рофлов", "рофлам", "рофлах",
    
    "вайб", "вайба", "вайбу", "вайбом", "вайбами", "вайбе",
    "вайбы", "вайбов", "вайбам", "вайбах",
}

class Feedback(BaseModel):
    name: str = Field(..., pattern="^.{2, 50}$")
    message: str = Field(..., pattern="^.{10, 500}$")

    @field_validator("message", mode="before")
    @classmethod
    def check_for_words(cls, v: str) -> str:
        lower_mess = v.lower()
        words = lower_mess.split()

        for word in words:
            clean_word = "".join(c for c in word if c.isalnum())
            if clean_word in banned_words:
                raise ValueError(f"вы написали запрещенное слово {clean_word}")
        return v

message_bd = []

@app.post('/feedback')
async def get_message(mes: Feedback):
    message_bd.append({"name": mes.name, "message": mes.message})
    return {"message": f"Спасибо, {mes.name}! Ваш отзыв сохранен."}

@app.get('/')
async def root():
    return message_bd

# запускать в /docs в feedback try out для записи сообщения, / try out для просмотра сообщений, прошедшых валидацию