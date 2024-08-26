original = list(input("Enter text: "))
mirror = ""
# Repeats from the last element in text to the first.
for i in range(len(original)-1,-1,-1):
    mirror += original[i]
print(mirror)