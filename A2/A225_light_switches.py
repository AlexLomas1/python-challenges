num_switches = int(input("Enter number of switches: "))
# Initialising list containing the current status of each light switch,
# where all switches start as being off (False).
switches = [False] * num_switches

while True:
    # Takes and splits the input into a list to use as limits.
    limits = input().split(" ")
    # If a limit is non-numerical, or there are not 2 limits, it stops
    # the loop.
    if len(limits) != 2 or not all(i.isnumeric() for i in limits):
        break
    start, end = int(limits[0]), int(limits[1])
    # Ensures starting limit is less than or equal to the ending limit.
    if start > end:
        start, end = end, start
    # Ensures limits are within valid range.
    if start < 0 or end >= num_switches:
        print("Error: limits outside of range")
    else:
        # Toggles switches in the specified range (inclusive).
        for i in range(start,end+1):
            switches[i] = not switches[i]

# Counts and outputs the number of switches that are currently on.
print(switches.count(True))