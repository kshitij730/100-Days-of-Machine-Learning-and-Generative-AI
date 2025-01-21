# Write a script that takes user input and performs basic arithmetic operations.

def main():
    print("Welcome to the Basic Arithmetic Calculator!")
    
    while True:
        try:
            # Take user input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Display operation options
            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            
            # Take user input for the operation
            choice = input("Enter the number corresponding to your choice (1/2/3/4): ").strip()
            
            # Perform the operation
            if choice == '1':
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
            else:
                print("Invalid choice. Please select a valid operation.")
            
            # Ask if the user wants to perform another calculation
            again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
