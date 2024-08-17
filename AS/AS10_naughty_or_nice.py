def naughty_or_nice(string):
    """
    Determine if a string is naughty or nice based on specific criteria.
    Return "Nice" if it contains at least 3 vowels, at least one letter
    appearing twice in a row, and does not contain any of the substrings
    "ab", "cd", "pq" or "xy". Otherwise, return "Naughty".
    """
    count, vowel_count = 0, 0
    double_letter, ab_cd_pq_xy = False, False
    string = list(string)
    while count < len(string) and not ab_cd_pq_xy:
        # Counts vowels in the string
        if string[count].lower() in ["a","e","i","o","u"]:
            vowel_count += 1
        # Necessary because next two if statements both use string[
        # Count+1], and if Count = len(string)-1 then string[Count+1]
        # does not exist.
        if count < len(string)-1:
            # Checks if there is a double letter.
            if string[count].lower() == string[count+1].lower():
                double_letter = True
            # Checks if any of the bad substrings are present.
            if (string[count]+string[count+1]) in ["ab","cd","pq","xy"]:
                ab_cd_pq_xy = True
        count += 1
    # Checks and returns whether the string is naughty or nice.
    if vowel_count >= 3 and double_letter and not ab_cd_pq_xy:
        return "Nice"
    else:
        return "Naughty"

# Opens text file, promptspal.txt is used simply for testing purposes.
with open("promptspal.txt") as text_file:
    # Reads and saves text file as a list, with each line as an element.
    # Could instead use text = (text_file.read()).split(" ") to seperate
    # file into words rather than lines.
    text = text_file.readlines()

# Counts number of naughty strings and nice strings
nice_count, naughty_count = 0, 0
for line in text:
    if naughty_or_nice(line) == "Nice":
        nice_count += 1
    else:
        naughty_count += 1

print("There are",nice_count,"nice strings in this text file")
print("There are",naughty_count,"naughty strings in this text file")