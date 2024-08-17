triangle_nums = [1]
# Function to calculate and store the next triangle number in the list
def next_triangle_num(n):
    triangle_nums.append(0.5*n*(n+1))

# Opens and reads the text file
with open("words.txt") as words:
    words_list = words.read()

triangle_word_count = 0

# Calculates the value of each word in words_list
for word in words_list:
    word_value = 0
    for letter in word:
        # ord(letter.upper())-64 returns the alphabetical position of 
        # letter (e.g. if letter is "a" it would return 1).
        word_value += ord(letter.upper())-64
    # Causes the next triangle number to be calculated if the current
    # value exceeds the highest stored triangle number.
    while word_value > triangle_nums[len(triangle_nums)-1]:
        next_triangle_num(len(triangle_nums)+1)
    if word_value in triangle_nums:
        triangle_word_count += 1

print("Number of triangle words in words.txt:",triangle_word_count)