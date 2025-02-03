import requests
import json

response = requests.get(
    'https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json'
    ,timeout=10)
print(type(response),"response:",response)
print(type(response.status_code),"response.status_code:",response.status_code)
print(type(response.json()),"response.json():",response.json())

with open('pathik.linkedin.json', 'r') as file:
    content = file.read()
data = content
print(type(data),"data:",data)
print(type(json.loads(data)),"json.loads(data):",json.loads(data))
