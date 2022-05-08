print("Welcome to the Rollercoaster!")

height = int(input("what is your height? "))
 
if height >= 120:
    print("you can ride")
     
    age = int(input("what is your age? "))

    if age < 12:
        bill = 5
        print("your ticket is 5$")
    elif age <= 18:
        bill = 7
        print("your ticket is  7$")
    else:
        bill = 12
        print("your ticket is 12$")
    want_photos = input("Do you want photo? Yes or NO.")

    if want_photos == "Yes":
        bill += 3
    
    print(f"your final bill is {bill}")


else:
    print("you can't ride.")