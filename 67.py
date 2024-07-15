import requests

data = {
    "title": "New task",
    "description": "This is a new task created via requests"
}

response = requests.post("http://127.0.0.1:5000/tasks", json=data)
