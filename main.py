from autogen_test import talk_to_autogen
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# a representation of a Discord Message
class DiscordMessage(BaseModel):
    message: str

@app.get("/")
async def home():
    return {"Hi Cold World"}


# endpoint to receive messages from discord bot and trigger ai response
@app.post("/discord-message")
async def receive_msg(request: DiscordMessage):
    response = talk_to_autogen(request.message)
    msg = response
    return msg
