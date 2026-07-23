from typing import List, Optional, TypedDict

class UserProfile(TypedDict):
    id : int
    name : str
    email : str
    bio : Optional[str]

def format_user_profile(users:List[UserProfile]) -> List:
    return [f" {u['name']}({u['email']})" for u in users]

users = [
    {
        "id":1,
        "name":"Ankush",
        "email":"ankush@gmail.com",
        "bio":None
    },
    {
        "id":2,
        "name":"Ankita",
        "email":"ankita@gmail.com",
        "bio":"On a trip."
    }
]

print(format_user_profile(users))