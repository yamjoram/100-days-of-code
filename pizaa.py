print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, L")

if size == " S ":
    bill = 15
    print("your bill is 15 $")

if size == "M" :
    bill = 20
    print("your bill is 20$")

if size == "L":
    bill = 25
    print("your bill is 25$")

add_pepperoni = input("Do you want pepperoni?")

if add_pepperoni == " Y":
    size == "S"
    bill += 2

else:
    bill += 3

extra_cheese = input("Do you want extra cheese? Y or N")

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is {bill}")
