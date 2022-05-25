
#print is your friend

pages = 0

word_per_page = 0
pages = int(input("number of pages: "))
word_per_page = int(input("number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)