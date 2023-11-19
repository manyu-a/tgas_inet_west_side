from fastapi import FastAPI
from pydantic import BaseModel

from DummyWatChecker import DummyWatChecker

whole_wat_checker = DummyWatChecker(0, 1, 500, 700, 4)
tv_wat_checker = DummyWatChecker(1, 0, 50, 100, 1)
airCon_wat_checker = DummyWatChecker(2, 0, 50, 100, 1)
oven_wat_checker = DummyWatChecker(3, 0, 50, 100, 1)
stove_wat_checker = DummyWatChecker(4, 0, 50, 100, 1)
refrigerator_wat_checker = DummyWatChecker(4, 0, 50, 100, 1)
gas_checker = DummyWatChecker(-1, 0, 100, 500, 1)
checker = {0: whole_wat_checker, 1: tv_wat_checker, 2: airCon_wat_checker,
           3: oven_wat_checker, 4: stove_wat_checker, 5: refrigerator_wat_checker, -1: gas_checker}
name = {1: "TV", 2: "エアコン", 3: "オーブン", 4: "ストーブ", 5: "冷蔵庫"}
yen_per_wat = 20
yen_per_gas = 215

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


@app.post("/api/wat_{id}")
def wat_all(id : int):
    return { "id": checker[id].id, "full": checker[id].amount, "per": checker[id].amount / checker[0].amount,
            "yen": checker[id].amount * yen_per_wat, "name": name[id]}

