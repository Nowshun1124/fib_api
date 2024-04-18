from fastapi import FastAPI

import fib


app = FastAPI()

@app.get("/fib/n=/{n}")
def read_number(n):
    if n.isdecimal() ==True:
        a = int(n)

        if a > 0:
            x = fib.fibnum(a)
            return {
                "result": x
            }
        else:
            return {
                "status": "400",
                "message": "Bad request."
            }
    else:
        return {
                "status": "400",
                "message": "Bad request."
            }
        