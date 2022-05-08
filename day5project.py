import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
symbols = ["!", "@", "#", "$", "^", "%", "&", "*"]

print("welcomw to the password generator")
nr_letters = int(input("How many letters you would like to enter?\n"))
nr_numbers = int(input("How many numbers you would like to enter?\n"))
nr_symbols = int(input("How many symbols you would like to enter?\n"))

password = []

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for num in range(1, nr_letters + 1):
    password += random.choice(numbers)

for sym in range(1, nr_symbols + 1):
    password += random.choice(symbols)

random.shuffle(password)
print(password)

p_password = ""
for char in password:
    p_password += char

print(f"your password is {p_password}")