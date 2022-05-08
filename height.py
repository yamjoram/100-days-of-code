student_height = input("enter the student height").split()


for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
    print(student_height)
   

total_height = 0
for height in student_height:
    total_height += height
print(total_height)

no_of_students = 0
for student in student_height:
    no_of_students += 1
print(no_of_students)

average = round(total_height/no_of_students)
print(average)


