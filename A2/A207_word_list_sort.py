# Allows user to input a word list, and splits it into a list with each 
# word as an element.
original_list = input("Enter the list of words: ").split()
# Sorts the word list into alphabetical order. key=str.lower is used so 
# that the sorting is case-insensitive (otherwise Z would precede a).
sorted_list = sorted(original_list,key=str.lower)
sorted_list = (" ".join(sorted_list))
# Creates and opens the file wordlist.txt for writing
with open("wordlist.txt","w") as word_list:
    # Saves the sorted word list to the file
    word_list.write(sorted_list)
