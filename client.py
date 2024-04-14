import requests

res = requests.post("http://127.0.0.1:8000/fib/?n=",
                    json={"n": 22})

print(res.status_code)
print(res.text)