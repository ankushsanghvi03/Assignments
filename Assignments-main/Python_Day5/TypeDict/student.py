from typing import TypedDict

class Student(TypedDict):
    id: int
    name: str
    age: int

student1 = Student(id=1, name="Alice", age=20)
student2 = Student(id=2, name="Bob", age=22)

print(student1)
print(student2)

#Type dict converts the result into dict fromat
#mypy catches the error before you ru the program