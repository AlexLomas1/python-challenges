def denary_to_roman(denary):
    """Converts denary number to Roman numerals and returns result."""
    values = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    # Dictionary mapping values and their corresponding Roman numeral.
    values_to_numerals = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    # Empty string created to hold the Roman numeral result.
    roman = ""
    for value in values:
        # Subtract current value from denary and add corressponding numeral
        # to roman until denary is less than current value.
        while denary >= value:
            denary -= value
            roman += values_to_numerals[value]
        # Exit loop early if the denary value has already been fully reduced.
        if denary == 0:
            break
    return roman

def roman_to_denary(roman):
    """Converts Roman numerals to denary and returns result."""
    # Dictionary mapping Roman numerals and their corresponding denary values.
    numerals_to_values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    # List of denary values corresponding to individual numerals in the input.
    values = [numerals_to_values[numeral] for numeral in roman]
    # Handles cases of subtractive notation (e.g. IV is -1+5 = 4).
    if len(roman) > 1:
        for i in range(0,len(values)-1):
            if values[i] < values[i+1]:
                values[i] = -values[i]
    return sum(values)

# Allows users to select whether to convert from denary to Roman numerals
# or vice versa, with validation.
choice = input("Would you like to convert from denary or Roman numerals?: ")
while choice.lower() not in ["denary","decimal","roman numerals","roman"]:
    print("Please enter either denary or roman numerals.")
    choice = input("Would you like to convert from denary or Roman numerals?: ")

if choice.lower() in ["denary","decimal"]:
    denary = int(input("Enter number to be converted to Roman numerals: "))
    print(denary_to_roman(denary))
else:
    roman = input("Enter roman numerals to be converted to denary: ")
    print(roman_to_denary(roman))