def duplicates_removal(original):
    """Return copy of original list with duplicate elements removed."""
    new_list = []
    for element in original:
        # Checks if current element is not a duplicate.
        if element not in new_list:
            new_list.append(element)
    return new_list

# Takes the users input as a list, with elements seperated by a space.
original_list = input("Enter elements of list: ").split(" ")
# Prints the list after removing duplicates.
print(duplicates_removal(original_list))