# Takes user input for original string and converts to a list.
original = list(input("Enter text to convert to Rövarspråket: "))
consonants = {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t",
              "v","w","x","y""z"}
converted = []
consonant_sequence = ""

for i in range(len(original)):
    if original[i].lower() not in consonants:
        # If previous element was a consonant, it is now added to converted .
        if consonant_sequence:
            # Adds the consonant(s) to converted in Rövarspråket format.
            converted.append(consonant_sequence+"o"+consonant_sequence.lower())
            consonant_sequence = ""
        # Adds current (non-consonant) element to converted.
        converted.append(original[i])
    else:
        # Stores consonant elements in consonant_sequence, to later 
        # convert them to Rövarspråket format. Used to deal with
        # consecutive consonants.
        consonant_sequence += original[i]
        # Ensures consonant(s) are added to converted even if final 
        # element of original is a consonant.
        if i == len(original)-1:
            converted.append((consonant_sequence+"o"+consonant_sequence.lower()))
        
print("".join(converted))