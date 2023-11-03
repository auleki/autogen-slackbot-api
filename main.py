#!/usr/bin/env python3.8
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"Hi Cold World"}

@app.post("/discord-message")
async def receive_msg():
    return { "Send Messgage to AI" }
# add endpoint to receive messages from slack webhook
# on receiving message from slack, feed that into AutoGen
