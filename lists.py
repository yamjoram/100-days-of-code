import random 
name_string = input("enter's all the name's")
names = name_string.split(",")
length_item = len(names)

random_items = random.randint(0, length_item)

person_that_will_pay = names[random_items]
print(person_that_will_pay)



