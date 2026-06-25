def show_menu():
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=============================")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = num1 / num2
        operation = "Division"
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
        continue

    print(f"{operation} result: {result}")
