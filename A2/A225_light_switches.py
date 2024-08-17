num_switches = int(input("Enter number of switches: "))
#Initialising list containing the current status of each light switch, all starting as being off
switches = [False] * num_switches

while True:
    #Takes and splits the input into elements in a list
    limits = input().split(" ")
    #If an input is non-numerical, or there are not 2 limits, it stops the loop
    if len(limits) != 2 or not limits[0].isnumeric() or not limits[1].isnumeric():
        break
    start, end = int(limits[0]), int(limits[1])
    #Ensures starting limit is less than or equal to the ending limit
    if start > end:
        start, end = end, start
    #Ensures limits are within valid range
    if start < 0 or end >= num_switches:
        print("Error: limits outside of range")
    else:
        #Reverses the statuses of the switches in the inputted range inclusive
        for i in range(start,end+1):
            switches[i] = not switches[i]

#Counts and ouputs the number of light switches which are currently on
print(switches.count(True))
