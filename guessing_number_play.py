
#global constants = value that you never planning on changing

#choose a random number between 1 and 100

from random import randint

logo = """                .__                                  __                                                                               
__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____      ____  __ __   ____   ______ ______    _________    _____   ____  
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \    / ___\|  |  \_/ __ \ /  ___//  ___/   / ___\__  \  /     \_/ __ \ 
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  / /_/  >  |  /\  ___/ \___ \ \___ \   / /_/  > __ \|  Y Y  \  ___/ 
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   \___  /|____/  \___  >____  >____  >  \___  (____  /__|_|  /\___  >
             \/          \/            \/     \/                 /_____/             \/     \/     \/  /_____/     \/      \/     \/ 
"""
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#function to check user's guess against actual answer.

def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1

    elif guess < answer:
        print("too low")
        return turns  - 1
    else:
        print(f"you got it: the answer is {answer}")

#make function to set difficulty.

def set_difficulty():
    level = input("choose a difficulty. type 'easy' or 'hard' ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def game():
    print(logo)
    print("guess the number")
    answer = randint(1, 100)

    print(f"the correct answer is {answer}")

    #let the user guess a number
    turns = set_difficulty()
 

    #repeat the guessing functionality if they get it wrong

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")

        guess = int(input("make a guess"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("guess again")
            
#track the number of turns and reduce by 1 if they get it wrong

game()


