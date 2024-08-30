# Initialising states to contain all possible states of the garage door.
states = ["CLOSED","OPENING","STOPPED_WHILE_OPENING","OPEN","CLOSING",
          "STOPPED_WHILE_CLOSING"]
# Stores the index of the door’s current state, initialised to CLOSED.
current_state = 0
blocked = False
while True:
    action = input("> ")
    # Actions other than block_cleared and cycle_complete for EMERGENCY
    # OPENING are ignored when a block is detected.
    if not blocked:
        if action == "button_clicked":
            # If the door is either closed or open, pressing button
            # causes door to start moving.
            if current_state in [0,3]: 
                current_state += 1
            # If the door is currently moving, pressing button causes
            # door to stop where it is.
            elif current_state in [1,4]:
                current_state += 1
            # If door is currently stopped, pressing button causes door
            # to start going in the opposite direction.
            elif current_state in [2,5]:
                current_state = (current_state + 2) % 6
        # If door is currently moving, cycle_complete causes it to
        # finish moving.
        elif action == "cycle_complete" and current_state in [1,4]:
            current_state = (current_state + 2) % 6
        elif action == "block_detected":
            blocked = True
            # If currently closing and a block is detected, changes
            # current state to emergency opening.
            if current_state == 4:
                current_state = 1
    elif action == "block_cleared":
        blocked = False
    # Allows for the cycle EMERGENCY_OPENING to be completed even while
    # a block is detected.
    elif action == "cycle_complete" and current_state == 1:
        current_state += 2
    # Outputs door's current state after every input.
    if not blocked:
        print("Door: {}".format(states[current_state]))
    else:
        if current_state == 1:
            print("Door: EMERGENCY_OPENING")
        else:
            print("Door: {}_BLOCKED".format(states[current_state]))