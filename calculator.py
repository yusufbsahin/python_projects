def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator...")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue

        print("Result:", result)
        print("---------------")

if __name__ == "__main__":
    calculator()
