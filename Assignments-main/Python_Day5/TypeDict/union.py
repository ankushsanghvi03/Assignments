#A company is building AI virtual Assistant
#It has to accept diff input format - text, image, audio

from typing import Union

def process_input(data: Union[str, bytes]) -> None:
    if isinstance(data,str):
        print("Processign Text: ", data)
    elif isinstance(data,bytes):
        print("Processing Image/Audio Bytes: ", data)
    
process_input("Artificial Intelligence")

process_input(b'\x89PNG\r\n')

#Uinion - One variable can accept differnet data types
#89 - Non printable byte used to identify PNG Image
#PNG - PNG Image
#\r - Carriage return
#\n - new line
#isinstance - for checking the input type


