'''
json modules
json.dumps() - Python Dict to JSON string
json.loads() - JSON string to Python Dict
''' 
import json
user = {
    "id": 101,
    "name": "ABC",
    "active": True,
    "skills": ["Python", "FASTApi"]
}

json_string = json.dumps(user)
print(json_string)
print(type(json_string))

json_dict = json.loads(json_string)
print(json_dict)
print(json_dict['name'])
print(type(json_dict))

