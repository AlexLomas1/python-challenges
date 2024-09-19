# Reads text file and stores its contents in an array, with each word as an element.
with open("if.txt") as file:
    words_list = file.read().split()
# Finds the number of words.
word_count = len(words_list)
# Finds the sum of the word lengths of all words in the file.
word_length_sum = 0
for word in words_list: 
    word_length_sum += len(word)

# Calculating average word length of file, and returns it rounded to 2 decimal places.
av_word_length = word_length_sum / word_count
print(f"Average word length: {round(av_word_length,2)}")