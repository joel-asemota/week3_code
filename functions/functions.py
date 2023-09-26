def add(num1, num2):
    result = float(num1) + float(num2)
    print(result)

num1 = 40
num2 = 30

add(num1, num2)

def subtract(num1, num2):
    result = float(num1) - float(num2)
    print(result)

input1 = input("Enter a number: ")
input2 = input("Enter a number: ")

inputcalc = input ("Enter a calculation: " )

if inputcalc == "add":
    add(input1, input2)
elif inputcalc == "subtract":
    subtract(input1, input2)
