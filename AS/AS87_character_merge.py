#Allows user to input the two strings to be merged. Strings are converted to lists so that the characters are seperated
word1 = list(input("Enter string 1: "))
word2 = list(input("Enter string 2: "))
#Initialises the two counts to zero
count1, count2 = 0, 0
#Intialises list to store the merged characters from the two strings
merged = [""] * (len(word1)+len(word2))
#Initialises current_string, used to alternate between the strings being added to merged
current_string = 1

#Iteration continue until both counts have reached the length of their respective strings
while count1 < len(word1) or count2 < len(word2):
    if current_string == 1:
        #Alternates value of current_string so that a character from the other string will be added next
        current_string = 2
        #Body of if statement will only occur if there are still characters from word1 to be added
        if count1 < len(word1):
            merged[count1+count2] = word1[count1]
            count1 += 1
    else:
        #Alternates value of current_string so that a character from the other string will be added next
        current_string = 1
        #Body of if statement will only occur if there are still characters from word2 to be added
        if count2 < len(word2):
            merged[count1+count2] = word2[count2]
            count2 += 1

#Converts merged to a string for the output
print("".join(merged))
