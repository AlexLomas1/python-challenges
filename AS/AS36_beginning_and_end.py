# Seperates user input into a list, with elements seperated by commas.
original = str(input("Enter list of items, seperated by commas: ")).split(", ")
# Creates a list containing only the first and last element of original.
beginning_and_end = [original[0],original[len(original)-1]]
print(beginning_and_end)