#RACE - Role, Action, Context, Expectation - list of inputs

from typing import Sequence

def process_management(message: Sequence[str]) -> None:
    print("Message Recieved.")

    for m in message:
        print(m)

texts = [
    "Hello",
    "How are you?",
    "Working with FASTApi"
]

text_tuple = (
    "Checking the input",
    "Tuple input",
    "Working or not."
)

process_management(texts)
process_management(text_tuple)