import random

user = int(input("enter the number: 1- 12 ")) 
count = 0
while count < 6:
    print("value of count ", count)
    dice1 = random.randrange(1,7)  
    dice2 = random.randrange(1,7) 
    total_dice = (dice1 + dice2) 
    print(total_dice)

    if total_dice == 7 and total_dice == user:
        print("lucky 7 you won")

    elif total_dice > 7 and user > 7  and user <= 12:
        print("over, you won")

    elif total_dice < 7 and user < 7:
        print("under, you won")

    else:
        print("you failed")
    count += 1