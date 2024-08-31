n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
# Creates empty 2d array with n rows and m columns.
board = [[""] * m for _ in range(n)]
# Initialising tile types.
tile = (".","*")
# Initialising current tile type index, for alternating between the two 
# tile types.
current = 0
for row in range(n):
    for column in range(m):
        board[row][column] = tile[current]
        current ^= 1 # Alternates current between 0 and 1.
    # If m is even, current needs to be alternated again after every row 
    # so that the first element of each row alternates.
    if m % 2 == 0:
        current ^= 1

# Prints the checkers board.
for row in board:
    print(" ".join(row))