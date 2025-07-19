import requests
res = requests.post("http://127.0.0.1:8000/api/bot", json={"message": "Who is Elon Musk?"})
print(res.json())
