from fastapi import FastAPI

app = FastAPI()

@app.get("/sri")
def greet():
    return {"message": "Hello World!"}