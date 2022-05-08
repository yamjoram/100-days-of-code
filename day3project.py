print(""" _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
""")
print("Welcome to Treasure island")
print("your mission is to find treasure")
choice1 = input('you\'re at the game, where do you want to turn?" "left" or "right",').lower()

if choice1 == "left":
    choice2 = input('which one you like to do? type "swim" or "wait"').lower()
    if choice2 == "wait":
        choice3 = input('which door you would like to open? "red" or "blue" or "yellow"').lower()
   
        if choice3 == "yellow":
            print("congrates you won")
        elif choice3 == "blue":
            print("you got beast, you\'re dead")
        else:
            print("sorry, game over")
    else:
        print("game over")
else:
    print("game over")    

