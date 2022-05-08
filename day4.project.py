import random


rock = '''____         \
| | | |/\       \
|_|_|_|\ \       \
|        /
\_______/            (  ( ) ) ( )  )
 \______\           ( ( ( ( )  )  ) )
 \       \         ( ( )) ) (   ) ( ( )
  \       \        ( (__.-.___.-.__) )
   \       \        /---._.---._.--- \
    \       \       \||   '  \'    ||/
     \       \       |||     _)   |||
      \       \       ||||///\\\||||
       \       \_____/ ||||\__/||||\___
        \             \ |||||||||| /   \
         \             \  ||||||  /     \
          \_____
'''
paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|    

'''

scissor = ''' 
_       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''

images = [rock, paper, scissor]
user_choice = int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissor"))
print(f"your choice is {user_choice}")
print(images[user_choice])
computer_choice = random.randint(0, 2)
print(f"computer choice is {computer_choice}")
print(images[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("you type invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("you won")

elif user_choice > computer_choice:
    print("you won")

elif user_choice == computer_choice:
    print("it's draw")

else:
    print("you lose")




