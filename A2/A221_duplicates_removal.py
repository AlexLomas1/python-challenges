def duplicates_removal(original):
    new_list = []
    for element in original:
        #Checks if current element of the original list is a duplicate
        if element not in new_list:
            #Only if the current element is not a duplicate will it be added to new_list
            new_list.append(element)
    #Returns the list without any duplicates
    return new_list

#Takes the users input as a list, with each element in the input seperated by a space
original_list = input("Enter elements of list: ").split(" ")
#Prints the list without any duplicates
print(duplicates_removal(original_list))