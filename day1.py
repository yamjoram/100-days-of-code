score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")

print("****************************************")

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
a_function(10)
print(a_variable)

print("*****************************************")

def outer_function(a, b):
    def inner_function(c,d):
       return c + d
    return inner_function(a, b)

result = outer_function(5, 10)
print(result)