val_1 = float(input("Enter first number:"))
val_2 = float(input("Enter second number:"))
operator = input("Choose an operator:(+ , - , * , /)")
if operator == "+":
    print("Addition =",val_1+val_2)
elif operator == "-":
    print("Subtraction = ", val_1-val_2)
elif operator == "*":
    print("Multiplication = ", val_1*val_2)
elif operator == "/":
    if val_2 == 0:
        print("A number cannot be divided by '0'.")
    else:
        print("Division = ", val_1/val_2 )