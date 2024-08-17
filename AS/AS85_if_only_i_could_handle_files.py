#Opening the files for reading
with open("if.txt") as file1, open("mam.txt") as file2:
    #Reading the files
    text1 = file1.read()
    text2 = file2.read()

#Initialising variables for counting
count = 0
if_counter1, if_counter2 = 0, 0
#Counting the number of times 'if' appears in each file
while count < len(text1)-1 or count < len(text1)-1:
    if count < len(text1)-1:
        if (text1[count]+text1[count+1]).lower() == "if":
            #Ensures words which include if (e.g. gift) are not included, but cases where 'if' is next to punctuation are included
            if ((count == 0 and not text1[count+2].isalpha()) #If count is 0, then cannot check [count-1]
                or (count == len(text1)-2 and not text1[count-1].isalpha()) #If count == len(text1)-2, then cannot check [count+2]
                or (not text1[count-1].isalpha() and not text1[count+2].isalpha())): #If isalpha() for either value is true, then the 'if' must be part of a longer word rather than 'if' by itself
                if_counter1 += 1
    if count < len(text2)-1:
        if (text2[count]+text2[count+1]).lower() == "if":
            #Ensures words which include if (e.g. gift) are not included, but cases where 'if' is next to punctuation are included
            if ((count == 0 and not text2[count+2].isalpha()) #If count is 0, then cannot check [count-1]
                or (count == len(text2)-2 and not text2[count-1].isalpha()) #If count == len(text2)-2, then cannot check [count+2]
                or (not text2[count-1].isalpha() and not text2[count+2].isalpha())): #If isalpha() for either value is true, then the 'if' must be part of a longer word rather than 'if' by itself
                if_counter2 += 1
    count += 1

#Opening the files for appending
with open("if.txt","a") as file1, open("mam.txt","a") as file2:
    #Appending the if counters to their respective files
    file1.write(str(if_counter1))
    file2.write(str(if_counter2))
File1 = open("if.txt","a")
File2 = open("mam.txt","a")

#Stating which file has more of the word 'if'
if if_counter1 > if_counter2:
    print("File 1 has more of the word 'if' than file 2")
elif if_counter2 > if_counter1:
    print("File 2 has more of the word 'if' than file 1")
else:
    print("Both files have the same amount of the word 'if'")
