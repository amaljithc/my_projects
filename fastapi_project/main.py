from fastapi import FastAPI 


app = FastAPI()

@app.get('/')
def home():
    return {"messages":"welcome to the world of fastapi"}