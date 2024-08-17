import random
# Opens the text file promptspal.txt for reading.
with open("promptspal.txt") as prompts:
    # Reads the file and stores its contents in a list, with each line
    # as an element.
    prompts_list = prompts.readlines()
    # Prints a random prompt.
    print(random.choice(prompts_list))