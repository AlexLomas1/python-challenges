alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]

def shift_alphabet(shift):
    shifted_alphabet = []
    for i in range(26):
        shifted_alphabet.append(alphabet[(i+shift)%26])
    return shifted_alphabet

def encrypter():
    original = str(input("Enter string to be encrypted: "))
    shift = int(input("Enter number of shifts: "))
    shifted_alphabet = shift_alphabet(shift)
    encrypted = ""
    for char in original:
        # If current character is not in the alphabet (e.g. a space), it is added
        # to encrypted unchanged.
        if not char.isalpha():
            encrypted += char
        else:
            upper = False
            # Checks if current character is upper case.
            if char.upper() == char:
                upper = True
            # Performs linear search for current character in alphabet, and if found
            # the character in shifted_alphabet with the same index is added to encrypted.
            for i in range(26):
                if char.lower() == alphabet[i]:
                    if upper:
                        encrypted += shifted_alphabet[i].upper()
                    else:
                        encrypted += shifted_alphabet[i]
                    break
    return encrypted

def decrypter():
    encrypted = str(input("Enter text to be decrypted: "))
    shift = int(input("Enter number of times it has been shifted: "))
    shifted_alphabet = shift_alphabet(shift)
    decrypted = ""
    for char in encrypted:
        # If current character is not in the alphabet (e.g. a space), it is added
        # to decrypted unchanged.
        if not char.isalpha():
            decrypted += char
        else:
            upper = False
            # Checks if current character is upper case.
            if char.upper() == char:
                upper == True
            # Performs linear search for current character in shifted_alphabet, and if
            # found the character in alphabet with the same index is added to decrypted.
            for i in range(26):
                if char.lower() == shifted_alphabet[i]:
                    if upper:
                        decrypted += alphabet[i].upper()
                    else:
                        decrypted += alphabet[i]
                    break
    return decrypted


choice = str(input("Would you like to encrypt or decrypt?: ")).lower()
if choice == "encrypt":
    print(encrypter())
elif choice == "decrypt":
    print(decrypter())