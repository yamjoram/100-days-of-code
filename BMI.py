height = float(input("what is the height in m? "))
weight = float(input("what is the weight in kg? "))
BMI = round(weight/height**2)
if BMI < 18.5:
    print(f"your bmi is {BMI}, you are underweight")
elif BMI < 25:
    print(f"your bmi is {BMI}, you are normal weight")
elif BMI < 30:
    print(f"your bmi is {BMI}, you are overwight")
elif BMI < 35:
    print(f"your bmi is {BMI}, you are obese")
else:
    print(f"your bmi is {BMI}, you are clinically obese.")
