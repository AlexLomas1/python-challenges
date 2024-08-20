import random

def bubble_sort(list_):
    """Perform a bubble sort on a list, and return the sorted list."""
    no_swaps = False
    end = len(list_)-1
    # Repeats until there have been no swaps or there are no more elements 
    # to check.
    while not no_swaps and end > 0:
        no_swaps = True
        for i in range(0,end):
            # Swaps elements if they aren't in ascending order.
            if list_[i] > list_[i+1]:
                list_[i], list_[i+1] = list_[i+1], list_[i]
                no_swaps = False
        end -= 1
    return list_

# Creates a random list and uses it to test the bubble_sort function.
test_list = []
for i in range(9):
    test_list.append(random.randint(0,1000))
print("Unsorted list:", test_list)
print("Bubble sorted list:", bubble_sort(test_list))