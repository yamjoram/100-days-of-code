print("Welcome to the tip calculator.")
total_bill = float(input("what was the total bill?"))
percentage = int(input("what percentage tip would you like to give?"))
tip_percentage = int( (percentage) / 100)
tip_given =  total_bill * tip_percentage
amount_given = tip_given + total_bill
bill_split = int(input("How many people to split the bill?"))
bill_splited = amount_given / bill_split
final_amount = round(bill_splited, 2)
print(f"each person should pay : {final_amount} " )