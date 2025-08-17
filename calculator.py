def calculator():
        print("THE SYMPLE CALCULATOR.")
        print("______________________")
        print("Operations are available:")
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")
        print("5. Exit")

        while True:
            try:
                choice = int(input("Enter your choice among them above :"))
                
                if choice == 5:
                    print("Thank you! The loop is going to exit")
                    break
                if choice not in(1,2,3,4):
                    print("Invalid input. Please select a correct choice.")
                    continue
                
                num1 = float(input("Enter your first number:"))
                num2 = float(input("Enter your second number:"))

                if choice == 1:
                    print(f"Result : {num1}+{num2} = {num1 + num2}")
                elif choice == 2:
                    print(f"Result: {num1}{num2} = {num1 - num2}")
                elif choice == 3:
                    print(f"Result: {num1}*{num2} = {num1 * num2}")
                elif choice == 4:
                    if num2 == 0:
                        print("Error! Division by Zero")
                    else:
                        print(f"Result: {num1}/{num2} = {num1/num2}")


            except ValueError :
                     print("Invalid input. Please enter numbers only")
            except Exception as e :
                     print(f"An error occured : {e}")


                     
        
        
calculator()
