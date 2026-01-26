print("Simple Calculator")

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operator = input("Enter an operator (+, -, *, /): ")
# nag buhat nako schwa!
    if operator == "+":
        result = num1 + num2
        print("Result:", result)

    elif operator == "-":
        result = num1 - num2
        print("Result:", result)
	#UPDATED NANI BRUH!

    elif operator == "*":
        result = num1 * num2
        print("Result:", result)

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid operator")

    choice = input("Do you want to calculate again? (y/n): ").lower()
    if choice != "y":
        print("Goodbye!")
        break

