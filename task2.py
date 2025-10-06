def calculator():
    print("Welcome to the simple calculator!")
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("That's not a valid number. Please try again.")
        return
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("That's not a valid number. Please try again.")
        return
    print("\nSelect an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    operation = input("Enter your choice (1, 2, 3, or 4): ")

    if operation == '1':
        result = num1 + num2
        print(f"\nThe result is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\nThe result is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\nThe result is: {result}")
    elif operation == '4':

        if num2 == 0:
            print("\nError: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"\nThe result is: {result}")
    else:
        print("\nInvalid choice. Please select a number from 1 to 4.")

calculator()