from tkinter import W


age = input("what is your age?")
int_age = int(age)

years_remaining = 90 - int_age
months_remaining = 12 * int_age
weeks_remaining = 52 * int_age
days_remaining = 365 * int_age
print(f"you have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months")