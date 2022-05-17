#calculator

#add

from operator import truediv


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

def calculator():

    num1 = int(input("what's the first number? : "))


    for operator in operations:
        print(operator)
    should_continue = True

    while should_continue:

        operator_symbol = input("which operator you need? ")
        num2 = int(input("what's the second number? : "))
        calculation_function = operations[operator_symbol]
        answer = calculation_function(num1, num2)


        print(f"{num1} {operator_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation: ") == "y":


            num1 = answer
        
        else:
            should_continue = False

            calculator()
        

calculator()