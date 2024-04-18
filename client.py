import requests

res = requests.get("http://127.0.0.1:8000/fib/n=/22")

print(res.status_code)
print(res.text)