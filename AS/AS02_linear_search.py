def linear_search(list_,item):
    """Perform a linear search. If item is found in list_, print the
    index of the item. Otherwise, print "Item not found"."""
    found = False
    for i in range(len(list_)):
        # Checks if current element matches item. If so, the current index is
        # printed, found is updated and the loop is exited.
        if list_[i] == item:
            print("Item found at index", i)
            found = True
            break
    if not found:
        print("Item not found")