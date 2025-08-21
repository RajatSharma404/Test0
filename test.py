import math
print("Welcome to the Python Calculator!")
print("Options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor division")
print("7. Exponentiation")
print("8. Square Root")
print("9. Logarithm (base 10)")
print("10. Sine")
print("11. Cosine")
print("12. Tangent")
print("13. Exit")
def calculator():
    while True:
        choice = input("\nChoose an operation (1-13): ")
        if choice == '13':
            print("Exiting the calculator. Goodbye!")
            break
        if choice in ['1', '2', '3', '4', '5','6','7']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        elif choice == '5':
            if num2 != 0:
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            else:
                print("Error: Cannot divide by zero.")
        elif choice == '6':
            if num2 != 0:
                print(f"Result: {num1} // {num2} = {num1 // num2}")
        elif choice == '7':
            print(f"Result: {num1} ^ {num2} = {math.pow(num1, num2)}")
        elif choice == '8':
            num = float(input("Enter the number: "))
            if num >= 0:
                print(f"Square root of {num} = {math.sqrt(num)}")
            else:
                print("Error: Cannot calculate the square root of a negative number.")
        elif choice == '9':
            num = float(input("Enter the number: "))
            if num > 0:
                print(f"Log base 10 of {num} = {math.log10(num)}")
            else:
                print("Error: Logarithm is undefined for numbers less than or equal to zero.")
        elif choice == '10':
            num = float(input("Enter the angle in degrees: "))
            print(f"Sine of {num}° = {math.sin(math.radians(num))}")
        elif choice == '11':
            num = float(input("Enter the angle in degrees: "))
            print(f"Cosine of {num}° = {math.cos(math.radians(num))}")
        elif choice == '12':
            num = float(input("Enter the angle in degrees: "))
            print(f"Tangent of {num}° = {math.tan(math.radians(num))}")
        else:
            print("Invalid input. Please enter a number between 1 and 11.")
        again = input("\nD6o you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break
calculator()