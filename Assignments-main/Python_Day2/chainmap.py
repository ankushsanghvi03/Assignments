from collections import ChainMap

dict1 = {"x": 10, "y": 20}
dict2 = {"y": 50, "z": 30}

cm = ChainMap(dict1, dict2)

print(cm)
print("Value of y: ", cm["y"])