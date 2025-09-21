print("Welcome to Simple Calculator!")

while True:
    # User input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter 1/2/3/4: ")
    
    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid choice!")

    # Continue or exit
    cont = input("Do you want to calculate again? (y/n): ").lower()
    if cont != "y":
        print("Thanks for using Simple Calculator! ")
        break
