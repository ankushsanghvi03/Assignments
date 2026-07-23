#AI Chatbot receiving mixed inputs - union, sequence

from typing import Union, Sequence

InputData = Union[str,bytes]

def chatbots(inputs:Sequence[InputData]):
    for item in inputs:
        if isinstance(item,str):
            print("User text: ", item)
        else:
            print("Image Uploaded: (", len(item), "bytes)") #(4 bytes)

conversation = (
    "Hi",
    "Show me nearby restaurants",
    b'\x89PNG',
    "Explain this image"
)
#b'\xff\xd8\xff' - 3 bytes - JPEG

chatbots(conversation)