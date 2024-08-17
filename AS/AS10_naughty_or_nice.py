#Function to determine if a string is considered Naughty or Nice
def naughty_or_nice(string):
    #Initialising local variables
    count, vowel_count = 0, 0
    double_letter, ab_cd_pq_xy = False, False
    #Converts string to a list
    string = list(string)
    while count < len(string) and not ab_cd_pq_xy:
        #Checks if current element in list is a vowel
        if string[count].lower() in ["a","e","i","o","u"]:
            vowel_count += 1
        #Necessary because next two if statements both use string[Count+1], and if Count = len(string)-1 then string[Count+1] does not exist
        if count < len(string)-1:
            #Checks if there is a double letter
            if string[count].lower() == string[count+1].lower():
                double_letter = True
            #Checks if any of the bad substrings are present
            if (string[count]+string[count+1]) in ["ab","cd","pq","xy"]:
                ab_cd_pq_xy = True
        count += 1
    #Checks from the variable values if the string is naughty or nice
    if vowel_count >= 3 and double_letter and not ab_cd_pq_xy:
        return "Nice"
    else:
        return "Naughty"

#Opens text file
#promptspal.txt is used (from AS86) simply because I don't have another text file to test code with
with open("promptspal.txt") as text_file:
    #Reads the text file and saves it in a list, with each line as an element
    #Could  instead use text = (text_file.read()).split(" ") to seperate file into words rather than lines
    text = text_file.readlines()

#Initialises counters for the number of nice and naughty strings
nice_count = 0
naughty_count = 0
#Checks if current string is considered naughty or nice, and updates counter variables accordingly
for line in text:
    if naughty_or_nice(line) == "Nice":
        nice_count += 1
    else:
        naughty_count += 1

print("There are",nice_count,"nice strings in this text file")
print("There are",naughty_count,"naughty strings in this text file")
