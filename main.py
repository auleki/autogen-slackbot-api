from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"Hi Cold World"}

# add endpoint to receive messages from slack webhook
# on receiving message from slack, feed that into AutoGen
