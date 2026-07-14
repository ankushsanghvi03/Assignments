Product = ["Laptop", "Mouse", "Keyboard"]
newProducts = ["Monitor", "Tablet", "Webcam"]

count = int(input("How many products do you want to add: "))

for i in range(count):
    prod = input("Enter product: ")
    Product.append(prod)

newList = Product + newProducts
print(newList)

if "Mouse" in newList:
    newList.remove("Mouse")
print(newList)

if "Webcam" in newList:
    newList.remove("Webcam")
print(newList)

print(newList.count("Laptop"))
print(newList.index("Monitor"))

newList.sort()
print(newList)

print(newList[::-1])

backUp = newList.copy()
print(backUp)