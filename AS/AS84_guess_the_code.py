import AS07_caesar_cipher as cc

encrypted = input("Enter caesar ciphered message to be decrypted: ")

with open("words.txt") as words:
    words_list = words.read()

# In order to determine which shift results in the most 'natural' string, every
# unique shift (excl. 0) is tried and the number of words in the resulting string
# that are also in words.txt are counted, with the string that contains the most words
# from words.txt being considered the most 'natural'.
most_words = -1
most_natural_string = ""
for shift in range(1, 26):
    decrypt_attempt = cc.decrypter(encrypted, shift)
    # Counts the number of words in decrypt_attempt that are in words.txt
    words_count = 0
    for word in decrypt_attempt.split():
        if word.upper() in words_list: # words.txt contents is all upper case.
            words_count += 1
    if words_count > most_words: 
        most_words = words_count
        most_natural_string = decrypt_attempt

print(most_natural_string)