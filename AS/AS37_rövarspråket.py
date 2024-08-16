# Takes user input for original string and converts to a list
original = list(input("Enter text to convert to Rövarspråket: "))
consonants = {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t",
              "v","w","x","y""z"}
converted = []
consonant_sequence = ""

for element in original:
    if element.lower() not in consonants:
        # If previous element was a consonant, it is now added to converted 
        if consonant_sequence:
            # Adds the consonant(s) to converted in Rövarspråket format
            converted.append(consonant_sequence+"o"+consonant_sequence.lower())
            consonant_sequence = ""
        # Adds current (non-consonant) element to converted
        converted.append(element)
    else:
        # Stores consonant elements in consonant_sequence, to later 
        # convert them to Rövarspråket format. Used to deal with
        # consecutive consonants.
        consonant_sequence += element
        
print("".join(converted))