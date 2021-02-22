import requests

BASE = "http://192.168.0.108:5000/messages/Python script"

response = requests.post(BASE, json = {"message":"Hello There!", "author":"Dipesh","chatRoom":"Python script"})
print(response.text)
response = requests.post(BASE, json = {"message":"Hello There123!", "author":"Dipesh123", "chatRoom":"Python script"})
print(response.text)

response = requests.post(BASE, json = {"message":"Hi! My name is Dipesh Mohanty rreggreregregregrger regregregerg re ergreger ergregregregergre regergergerge", "author":"Dipesh Mohanty","chatRoom":"chatRoom1"})
print(response.text)

response = requests.get(BASE)
print(response.json())
