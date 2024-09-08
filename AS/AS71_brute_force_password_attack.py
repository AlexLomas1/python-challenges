import random
import time
import string

# Initialising list of characters, with 94 different characters.
characters = list(string.ascii_letters + string.digits + string.punctuation)

def create_password(n):
    """Generate aand return a random password which is n characters long."""
    password = ""
    for _ in range(n):
        password += random.choice(characters)
    print(f"Password: {password}")
    return password

def brute_force_attack(password):
    """Run every possible combination of characters from list characters until"""
    # Stores whether the password has cracked or not.
    cracked = False
    # Initialising length to 1.
    length = 1
    # Stores number of attempts until password has been cracked.
    attempts = 0
    # Stores current index of each character in current_attempt. Number 
    # of elements matches value of length.
    current_char_index = [0]
    start_time = time.time() # Starting timer.
    while not cracked:
        try:
            attempts += 1
            # Creating new guess.
            current_attempt = ""
            for i in range(length):
                current_attempt += characters[current_char_index[i]]
            # If passsword has been found.
            if current_attempt == password:
                # Finding time taken to crack password, rounded to 1dp.
                time_taken = round(time.time() - start_time, 1) 
                print(f"Password cracked in {attempts} attempts, or {time_taken} seconds.")
                cracked = True
            else:
                # Incrementing current_char_index if password not found.
                for i in range(length-1, -1, -1):
                    if current_char_index[i] < len(characters) - 1:
                        current_char_index[i] += 1
                        break
                    else:
                        # If all possible values at current length have
                        # been exhausted, length is increased by 1 and 
                        # current_char_index is initialised for new length.
                        if i == 0:
                            length += 1                            
                            current_char_index = [0 for _ in range(length)]
                        else:
                            current_char_index[i] = 0
        # Used to allow the brute force attack to be ended early.
        except KeyboardInterrupt:
            return

num_of_chars = int(input("Enter number of characters for generated password: "))
brute_force_attack(create_password(num_of_chars))