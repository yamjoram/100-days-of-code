import random


def deal_card():
    """returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculator_score(cards):

    """take a list of cards and return a score from cards"""

    if sum(cards) == 21 and len(cards) == 2:
     return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_cards = []
computer_cards = []
is_game_over = False

for _ in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_cover:

    user_score = calculator_score(user_cards)
    computer_score = calculator_score(computer_cards)

    print(f"your cards is {user_cards} and your score is {user_score}")
    print(f"computer's first cards are {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_cover = True
    else:

while computer_score != 0 and computer_score < 17 :
    computer_cards.append(deal_card())
    computer_score = calculator_score(computer_cards)
    
        user_should_deal = input("type 'y' to get another card, type 'n' to pass")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_cover = True

    

        


    

