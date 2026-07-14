numbers = list(map(int, input("Enter a list of integers seperated by spaces: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))

print("Squared even numbers: ", squared_even_numbers)