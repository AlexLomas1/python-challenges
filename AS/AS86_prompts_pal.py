import random
#Opens the text file promptspal.txt for reading
with open("promptspal.txt") as prompts:
    #Reads the file and stores its contents in an array, with each line as an element in the array
    prompts_list = prompts.readlines()
    #Prints a random element from prompts_list
    print(random.choice(prompts_list))