import time

start = time.time()

original_list = []

with open("10000words.txt","r") as file: 
    # Reads the file, each word is one line.
    for line in file:
        original_list.append(line.strip()) 

longest_length = 0 

# Words from original_list are sorted into 2d list new_list by length. new_list[0] is left empty
# as a consequence, but it prevents having to decrease length by 1 every time to access words of
# that length. There are no words in the file of length 20 or more.

new_list = [[] for _ in range(20)]
for word in original_list:
    length = len(word)
    if length > longest_length:
        longest_length = length
    new_list[length].append(word)

# Converts new_list to a list of sets.
word_sets = [set(list) for list in new_list]

def interlock(word1, len1, word2, len2):
    """Takes alternating letters from each word to form a new string, and returns this
    string."""
    interlocked = [word1[0],word2[0]]
    i, j = 1, 1
    while i < len1 or j < len2:
        if i < len1:
            interlocked.append(word1[i])
            i += 1
        if j < len2:
            interlocked.append(word2[j])
            j += 1
    return "".join(interlocked)

interlock_pairs = [] # Stores each pair of words that interlock to make a new word + the new word.
interlock_count = 0 # Counts number of interlocking pairs found.

count = 0
for len1 in range(1,longest_length):
    # Prevents len1 + len2 exceeding longest_length, as there is no point in trying any words
    # together if they result in a word longer than there is in the file.
    for len2 in range(1,longest_length-(len1-1)):
        # Tries each word of length len1 with each word of length len2. 
        for word1 in word_sets[len1]:
            for word2 in word_sets[len2]:
                if word1 != word2: # For when len1 == len2.
                    interlocked = interlock(word1, len1, word2, len2)
                    # Checks if this is a valid interlocking pair.
                    if interlocked in word_sets[len1+len2]:
                        interlock_pairs.append((word1, word2, interlocked))
                        interlock_count += 1

end = time.time()

print(interlock_pairs)

print(f"Time taken: {end-start}. {interlock_count} interlocking pairs found.")