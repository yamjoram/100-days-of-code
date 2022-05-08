
import math

def paint_cal(height, width, coverage):
    num_of_cans = math.ceil((height*width)/coverage)
    print(f"you need {num_of_cans} cans")

h = int(input("enter the height"))
w = int(input("enter the width "))
c = 5

paint_cal(height=h, width=w, coverage=c)


