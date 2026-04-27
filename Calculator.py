def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def clear():
    return 0


def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return "Invalid Operator!"


def main():
    print("=== Simple Calculator ===")

    while True:
        print("\nOptions:")
        print("1. Calculate")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose option (1/2/3): ")

        if choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                result = calculate(num1, operator, num2)
                print("Result:", result)

            except ValueError:
                print("Error: Invalid number input!")

        elif choice == "2":
            print("Calculator cleared!")

        elif choice == "3":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()