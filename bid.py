logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"winner is {winner}")

while not bidding_finished:
    bids = {}
    name = input("who wants to bid ")
    amount = int(input("amount you wat to bid? "))
    bids[name] = amount
    anyone = input("anyone left who wants to bid? ")

    if anyone == "no":
        bidding_finished = True

        find_highest_bidder(bids)

    elif anyone == "yes":
         clear()
    


