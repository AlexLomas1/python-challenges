grid = [[1,2,3],[4,5,6],[7,8,9]]
valid_moves = {1,2,3,4,5,6,7,8,9}
winner = ""

def win_check(player, grid):
    """Check if current player has met the requirements to win the game."""
    # Checks if the player has 3 in a row horizontally or vertically.
    for i in range(3):
        if (all(grid[i][j] == player for j in range(3)) or
        all(grid[j][i] == player for j in range(3))):
            return True
    # Checks if the player has 3 in a row diagonally.
    if ((grid[0][0] == player and grid[1][1] == player and grid[2][2] == player) or
        (grid[2][0] == player and grid[1][1] == player and grid[0][2] == player)):
        return True
    return False

def player_turn(player, grid, valid_moves):
    """Take current player's move and update the grid accordingly."""
    player_num = "1" if player == "X" else "2"
    print("Player "+player_num+"'s turn")
    # Validates move
    while True:
        try: 
            move = int(input("Enter space in grid: "))
            if move in valid_moves:
                # Updates grid.
                grid[(move-1)//3][(move-1)%3] = player
                valid_moves.remove(move)
                break
            else:
                print("This is not a valid move, please try again")
        except ValueError:
            print("This is not a valid input, please enter a number 1-9")

# Explains the rules
print("This is the grid: ")
for row in grid:
    print(row)
print("Player 1 is X, Player 2 is O. Each player will take turns to fill a space in the grid with their symbol.")
print("To do so you must enter the number corresponding to a free space in the grid.")
print("The first player to get 3 of their symbol in a row on the grid wins.")

# Loop continues until there are no more possible moves or it is broken internally due to a player winning.
while valid_moves:
    for player in ["X","O"]:
        if valid_moves:
            player_turn(player, grid, valid_moves)
            # Prints the updated grid.
            for row in grid:
                print(row)
            # Makes a blank space between turns, just because I think it looks nicer.
            print("")
            # Checks if current player has won. The loop is ended and the winner variable updated to player if so
            if win_check(player, grid):
                winner = player
                break
    if winner:
        break

if winner == "X":
    print("Player 1 wins!")
elif winner == "O":
    print("Player 2 wins!")
else:
    print("It is a tie")
