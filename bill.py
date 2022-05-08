import random
names = input("enter all the names ")
names_split = names.split(", ")
#name_length = len(names_split) 
#random_choice = random.randint(0, name_length - 1)

person_that_will_pay = random.choice(names_split)

print(person_that_will_pay + " is going to pay the bill.")