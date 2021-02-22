import requests


BASE = "http://192.168.0.108:5001/chatRooms/"

response = requests.post(BASE, json = {"chatRoomName": "Python script"})
print(response.text)


response = requests.get(BASE)
print(response.json())