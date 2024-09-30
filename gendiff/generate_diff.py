import json


with open ('file1.json', 'r') as file1:
    data1 = json.load(file1)

with open ('file2.json', 'r') as file2:
    data2 = json.load(file2)

print(data1)

print(data2)