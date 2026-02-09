a = float(input("Enter first number: "))
operator = input("Enter operator(+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("Error: Division by zero")
    else:
        print(a / b)
else :
    print("Please enter a valid operator")
print()