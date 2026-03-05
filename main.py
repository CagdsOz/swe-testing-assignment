from calculator import Calculator

calc = Calculator()

while True:
    a = float(input("First number: "))
    op = input("Operator (+ - * /): ")
    b = float(input("Second number: "))

    if op == "+":
        print(calc.add(a,b))
    elif op == "-":
        print(calc.subtract(a,b))
    elif op == "*":
        print(calc.multiply(a,b))
    elif op == "/":
        try:
            print(calc.divide(a,b))
        except ValueError:
            print("Division by zero")