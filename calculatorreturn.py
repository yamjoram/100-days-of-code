#calculator

#add

def add(n1 , n2):
    return n1 + n2

#subtract 

def subtract(n1, n2):
    return n1 - n2

#multiply

def multiply(n1, n2):
    return n1 * n2

#divide 

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("what's the first number? : "))
num2 = int(input("what's the second number? : "))

for operator in operations:
    print(operator)

operator_symbol = input("which operator you need? ")

calculation_function = operations[operator_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operator_symbol} {num2} = {answer}")