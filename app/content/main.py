from fastapi import FastAPI
from pydantic import BaseModel

from DummyWatChecker import DummyWatChecker

class User(BaseModel):
    name: str

class Prime(BaseModel):
    val: str

whole_wat_checker = DummyWatChecker(0, 1, 400, 600, 4)

app = FastAPI()

@app.get("/api")
def api_root():
    return {"Hello": "World"}

@app.post("/api/greetings")
def greetings(user: User):
    return { "message": f"こんにちは{user.name}さん" }

@app.post("/api/wat_full")
def wat_full():
    return { "id:": whole_wat_checker.id, "full:": whole_wat_checker.amount }

