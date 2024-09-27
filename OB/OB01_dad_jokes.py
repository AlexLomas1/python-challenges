import random

class DadJoke:
    def __init__(self, prompt, answer):
        """Intitialise the DadJoke object."""
        self.prompt = prompt
        self.answer = answer
    
    def print_joke(self):
        """Print self.prompt, give the user the opportunity to guess the answer,
        and then print self.answer"""
        print(self.prompt)
        input()
        print(self.answer)

# Stores the contents of DadJokes.txt in list dad_jokes, with each element as one
# line and with all \n removed.
with open("DadJokes.txt") as file:
    dad_jokes = file.readlines()
    dad_jokes = [joke.strip("\n")for joke in dad_jokes]

# Creates DadJoke objects from file contents and stores them in a list.
jokes_list = []
for i in range(0,len(dad_jokes),2):
    joke = DadJoke(dad_jokes[i], dad_jokes[i+1])
    jokes_list.append(joke)

# Calls print_joke() for a random DadJoke object in jokes_list
random.choice(jokes_list).print_joke()