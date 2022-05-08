print("Welcome to the rollercoaster!")
height = int(input("what is the height in cm? "))

if height >= 140 :
    print("you can ride")
    age = int(input("what is your age?"))
    if age < 12:
        print("please pay $5.")
    elif age <= 18:
       print("please pay $7.") 
    else:
        print("please pay $12.")

else:
    print("you can't ride")