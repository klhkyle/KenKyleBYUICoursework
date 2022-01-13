"""
File: W02ProveTicTacToe.py
Author: Ken Kyle
CSE 210 - Week 02 - Tic-Tac-Toe
"""
import subprocess as sp

def prompt(grid, turn):
    selection = int(input(f"{turn}'s turn to choose a square (1-9): "))
    grid[selection - 1] = turn
    return grid[selection]

def createGrid():
    grid = []
    for square in range(10):
        grid.append(square + 1)
    return grid

def displayGrid(grid):
    sp.call('cls', shell=True)
    print(f'''
     {grid[0]} | {grid[1]} | {grid[2]}
    ---+---+---
     {grid[3]} | {grid[4]} | {grid[5]}
    ---+---+---
     {grid[6]} | {grid[7]} | {grid[8]}
    ''')

def gameOver(grid):
    if ((grid[0] == "X" and grid[1] == "X" and grid[2] == "X") or
        (grid[3] == "X" and grid[4] == "X" and grid[5] == "X") or
        (grid[6] == "X" and grid[7] == "X" and grid[8] == "X") or
        (grid[0] == "X" and grid[3] == "X" and grid[6] == "X") or 
        (grid[1] == "X" and grid[4] == "X" and grid[7] == "X") or 
        (grid[2] == "X" and grid[5] == "X" and grid[8] == "X") or
        (grid[0] == "X" and grid[4] == "X" and grid[8] == "X") or
        (grid[2] == "X" and grid[4] == "X" and grid[6]== "X")):
        return "X"
    
    if ((grid[0] == "O" and grid[1] == "O" and grid[2] == "O") or
        (grid[3] == "O" and grid[4] == "O" and grid[5] == "O") or
        (grid[6] == "O" and grid[7] == "O" and grid[8] == "O") or
        (grid[0] == "O" and grid[3] == "O" and grid[6] == "O") or 
        (grid[1] == "O" and grid[4] == "O" and grid[7] == "O") or 
        (grid[2] == "O" and grid[5] == "O" and grid[8] == "O") or
        (grid[0] == "O" and grid[4] == "O" and grid[8] == "O") or
        (grid[2] == "O" and grid[4] == "O" and grid[6]== "O")):
        return "O"

    if (grid[0] != 1 and grid[1] != 2 and grid[2] != 3 and 
        grid[3] != 4 and grid[4] != 5 and grid[5] != 6 and 
        grid[6] != 7 and grid[7] != 8 and grid[8] != 9):
        return "Draw"

    return ""

def main():
    """
    Starts the program.
    """
    grid = createGrid()
    count = 1
    turn = "X"
    endGame = ""
    while endGame == "":       
        displayGrid(grid)
        prompt(grid, turn)
        if (count % 2) == 0:
            turn = "X"
        else:
            turn = "O"
        count += 1
        endGame = gameOver(grid)  

    sp.call('cls', shell=True)
    displayGrid(grid)
    if endGame == "Draw":
        print("The Game is a DRAW!")
    else:
        print((f"\nCongratulations {endGame}! You are the Winner!")) 

if __name__ == "__main__":
    main()