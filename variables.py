from base64 import b16decode


a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)