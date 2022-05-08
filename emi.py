row1 = ["🙂", "😀", "😃"]
row2 = ["😄", "😁", "😅"]
row3 = ["😆", "🤣", "😂"]

total_row = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("where you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])
total_row[vertical - 1][horizontal - 1] = "A"

print(f"{row1}\n{row2}\n{row3}")


