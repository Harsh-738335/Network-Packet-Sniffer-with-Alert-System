import json

def authenticate(username, password):
    with open("users.json", "r") as f:
        users = json.load(f)
    return users.get(username) == password
