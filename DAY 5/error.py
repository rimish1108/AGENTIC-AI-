try:
    num1 = int(input("Enter Number 1 = "))
    num2 = int(input("Enter Number 2 = "))
    try:
        result = num1 / num2
        print("Result", result)
    except ZeroDivisionError:
        print("You Cannot divide with 0")
except ValueError:
    print("You must provide a valid input")