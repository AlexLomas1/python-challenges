import random

def random_alphabet_generator(alphabet):
    """Generate and return a list containing all letters in the alphabet,
    in a random order, without repition."""
    random_alphabet = alphabet.copy()
    # Shuffles random_alphabet so letters are in a random order.
    random.shuffle(random_alphabet)
    return random_alphabet

def substitution_cipher(plain):
    """Encrypt a message using a substitution cipher with a randomly sequenced alphabet,
    and return the encrypted message."""
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
            "q","r","s","t","u","v","w","x","y","z"]
    random_alphabet = random_alphabet_generator(alphabet)
    encrypted = ""
    for char in plain:
        # If current character is not a letter (e.g. a space, punctuation), it is added
        # to encrypted unchanged.
        if not char.isalpha():
            encrypted += char
        else:
            # Checks if current char is upper-case.
            upper = False
            if char == char.upper():
                upper = True
            # Linear search for char in alphabet.
            for i in range(26):
                if char.lower() == alphabet[i]:
                    # If char is upper-case, the corresponding character added to encrypted
                    # is as well.
                    if upper:
                        encrypted += random_alphabet[i].upper()
                    else:
                        encrypted += random_alphabet[i]
                    # Loop is broken when char is found, so there are no redundant iterations.
                    break
    return encrypted

if __name__ == "__main__":
    plain_text = input("Enter text to be encrypted: ")
    print(substitution_cipher(plain_text))