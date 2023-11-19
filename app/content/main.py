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
yen_per_gas = 20

yen_per_wat_hour = [20, 10, 30]

whole_wat_hour = [200, 150, 350]
tv_wat_hour = [20, 15, 35]
airCon_wat_hour = [15, 25, 30]
oven_wat_hour = [30, 15, 25]
stove_wat_hour = [10, 35, 25]
refrigerator_wat_hour = [30, 15, 15]
gas_hour = [40, 80, 290]
hour_dict = {0: whole_wat_hour, 1: tv_wat_hour, 2: airCon_wat_hour,
        3: oven_wat_hour, 4: stove_wat_hour, 5: refrigerator_wat_hour, -1: gas_hour}




class User(BaseModel):
    name: str

class Prime(BaseModel):
    val: str


app = FastAPI()

@app.get("/api")
def api_root():
    return { "Hello": "World" }

@app.post("/api/greetings")
def greetings(user: User):
    return { "message": f"こんにちは{user.name}さん" }


@app.post("/api/gas_full")
def gas_full():
    return { "id": gas_checker.id, "full": gas_checker.amount, "yen": gas_checker.amount * yen_per_gas }

@app.post("/api/wat_full")
def gas_full():
    return { "id": whole_wat_checker.id, "full": whole_wat_checker.amount, "yen": whole_wat_checker.amount * yen_per_wat}

@app.post("/api/wat_other")
def wat_other():
    all_checker_amount = 0
    for checker_element in checker.keys():
        if (checker_element <= 0):
            continue
        
        all_checker_amount += checker[checker_element].amount
    other_amount = whole_wat_checker.amount - all_checker_amount
    return { "id": -2, "full": other_amount, "per": ((other_amount * 1000) // checker[0].amount) / 10,
            "yen": other_amount * yen_per_wat, "name": "その他" }

@app.post("/api/wat_{id}")
def wat_all(id : int):
    return { "id": checker[id].id, "full": checker[id].amount, "per": ((checker[id].amount * 1000) // checker[0].amount) / 10,
            "yen": checker[id].amount * yen_per_wat, "name": name[id] }

@app.post("/api/elec_total_hour{hour}")
def elec_total_hour(hour: int):
    return { "id": 0, "full": hour_dict[0][hour], "per": ((hour_dict[0][hour] * 1000) // sum(hour_dict[0])) / 10,
            "yen": hour_dict[0][hour] * yen_per_wat_hour[hour]}
    
@app.post("/api/gas_total_hour{hour}")
def gas_total_hour(hour: int):
    return { "id": -1, "full": hour_dict[-1][hour], "per": ((hour_dict[-1][hour] * 1000) // sum(hour_dict[-1])) / 10,
            "yen": hour_dict[-1][hour] * yen_per_gas}

@app.post("/api/elec_hour{hour}_wat_{id}")
def elec_hour_wat(hour: int, id: int):
    return { "id": id, "full": hour_dict[id][hour], "per": ((hour_dict[id][hour] * 1000) // hour_dict[0][hour]) / 10,
            "yen": hour_dict[id][hour] * yen_per_wat_hour[hour], "name": name[id] }
    
@app.post("/api/elec_hour{hour}_other")
def wat_other(hour: int):
    all_wat_hour_amount = 0
    for hour_element in hour_dict.keys():
        if (hour_element <= 0):
            continue
        all_wat_hour_amount += hour_dict[hour_element][hour]
    other_hour_amount = hour_dict[0][hour] - all_wat_hour_amount
    return { "id": -2, "full": other_hour_amount, "per": ((other_hour_amount * 1000) // hour_dict[0][hour]) / 10,
            "yen": other_hour_amount * yen_per_wat_hour[hour], "name": "その他" }
