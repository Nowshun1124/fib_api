from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import fib


app = FastAPI()

class Number(BaseModel):
    n: int

@app.post("/fib")
async def read_number(number: Number):
    if number.n > 0:
        x = fib.fibnum(number.n)
        return {
            "result": x
            }
    else:
        return {
            "status": "400",
            "message": "Bad request."
            }