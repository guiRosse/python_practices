import os

def cls():
    """Function made for clearing the console screen"""
    os.system("cls")

cls()
#   Add
def add(n1, n2):
    return n1 + n2
#   Substract
def substract(n1, n2):
    return n1 - n2
#   Multiply
def multiply(n1, n2):
    return n1 * n2
#   Divide
def divide(n1, n2):
    return n1 / n2
num1 = 0
num2 = 0
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide, 
    }
num1 = int( input("Num1: "))
num2 = int( input("Num2: "))

print(f"Num1 is {num1} and Num2 is {num2}")

print("Choose an operation from the operations below:")
for symbol in operations:
    print(symbol)
ops = input("\nSelected operation: ")
function = operations[ops](num1, num2)
# print(function)
print(f"\nAnswer is {function}")