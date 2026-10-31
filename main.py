print("--- Welcome to the continuous calculator ---")

while True:
    print("\n1. Addition (+)")
    print("2. Subtract (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit from the calculator")


    choice = input("Choose the operation number (1/2/3/4/5): ")

    if choice == '5':
        print("Bye! Thank you for using the calculator.")
        break  

  
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        if choice == '1':
            print(f"The result: {num1 + num2 + num3}")
        elif choice == '2':
            print(f"The result: {num1 - num2 - num3}")
        elif choice == '3':
            print(f"The result: {num1 * num2 * num3}")
        elif choice == '4':
            if num2 != 0 and num3 != 0:
                print(f"The result: {num1 / num2 / num3}")
            else:
                print("Error: Cannot be divided by zero!")
    else:
        print("The choice is incorrect, please select a number from the list.")
