from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str

class Prime(BaseModel):
    val: str

app = FastAPI()

@app.get("/api")
def api_root():
    return {"Hello": "World"}

@app.post("/api/greetings")
def greetings(user: User):
    return { "message": f"こんにちは{user.name}さん" }

@app.post("/api/eratosthenes")
def eratosthenes_base(prime: Prime):
    def eratosthenes(n):
        is_prime = ([False, True] * (n//2+1))[0: n+1]
        is_prime[1] = False
        is_prime[2] = True
        for i in range(3, n+1, 2):
            if not(is_prime[i]):
                continue
            if i*i > n:
                break
            for k in range(i*i, n+1, i):
                is_prime[k] = False
        return is_prime
    val = prime.val
    flag = False
    try:
        val = int(val)
    except Exception as e:
        flag = True
    
    if flag or val <= 1:
        return { "prime_bool": f"{val}は有効な整数ではありません" }
    try:
        val = int(val)
        ret = eratosthenes(val)[val]
        if ret:
            msg = "です"
        else:
            msg = "ではありません"

        return { "prime_bool": f"{val}は素数{msg}" }

    except Exception as e:
        return { "prime_bool": f"未知のエラー：{e}" }
    
    # app\content\main.py