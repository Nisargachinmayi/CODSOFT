def main():
    print("Simple Calculator")

    # Prompt user for the first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Prompt user for the second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Display operation choices
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt user for operation choice
    while True:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = num1 / num2

    # Display result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()