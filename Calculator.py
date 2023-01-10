from ast import operator


first =input("Enter first Number:")
operator =input("enter operator (+,-,*,/,%):")
second =input("Enter Second Number:")

first =int(first)
second =int(second)

if operator== "+":
    print(first + second)
elif operator== "-":
    print(first - second)
elif operator== "*":
    print(first * second)
elif operator== "/":
    print(first / second)
elif operator== "%":
    print(first % second)
else:
    print("Invalid Operation")