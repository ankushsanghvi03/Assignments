def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

def main():
    print("==============Simple Calculator==============")
    print("Addition:")
    print("Subtraction:")
    print("Multiplication:")
    print("Division:")

    choice = input("Enter your choice (1-4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result of addition is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result of division is: {divide(num1, num2)}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
        