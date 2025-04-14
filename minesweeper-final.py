# Minesweeper - Final Project
# Abat, Arian Dave S.
# Banganan, Grach B.
# 
# Date Created: April 09, 2025
# Current Version: 1.3.04.14.25
# (+) Added New Game Difficulty
# (+) Added Command to Give Up
# 
# 
# Old Version: 1.2.04.13.25
# Features:
# (+) Improved the Method for Printing the Board
# (+) Added Guide Letters
# (+) Added Method that Reveals Cells
# (+) Added Flagging Method
# (+) Added Win Condition
# (+) Added Option to Play Again
# (+) Added Method to See Best Time
# (+) Added Colors to the UI
# (+) Added Timer
# (+) Added Debug Command (Shows All Mines)
# (+) Added Method that can Compare Best Time
# (+) Improved Flow of Program
# (+) Improved Player Move Method
# (+) Handles Some Special Cases
# Lines of code: 400+
# 
# 
# Old Version: 1.1.04.09.25
# Features:
# (+) Initial Menu Design
# (+) Initial Board Design
# (+) Added General Instructions
# (+) Added Different Game Difficulties
# (+) Added Method to Generate Bombs
# (+) Added Method to Generate Board
# (+) Added Partially Working Move Validation Method
# (+) Handles some special cases
# (+) Adjusts Board after Generating
# (?) Special Cases in Move Validation not fixed
# Lines of code: 100+
# 
# 
# WIP:
# Menu Design
# Points

import random
import time
from colorama import Fore, Back, Style, init

init(autoreset = True)

mainMenu = """
{0}Welcome to minesweeper{1}
{0}[1] Play{1}
{0}[2] Exit{1}
""".format(Fore.CYAN, Style.RESET_ALL)

modeMenu = """
{0}Select Game Mode{1}
{0}[1] Easy{1}
{0}[2] Medium{1}
{0}[3] Hard{1}
{0}[4] Very Hard{1}
""".format(Fore.CYAN, Style.RESET_ALL)

board = []

cloneBoard = []

guide = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

flagCount = 0
totalFlags = 0

gameOver = False

bestTime = None

debugMode = True

def main_loop():
    while True:
        print(modeMenu)

        try:
            choice = int(input("Choice: "))

        except ValueError:
            print("Please enter only integer!")
            continue
        
        select_gamemode(choice)
        
        while True:
            playAgain = input("Do you want to play again? (Y/N): ").lower().strip()

            if playAgain == "y":
                board.clear()
                cloneBoard.clear()
                break

            elif playAgain == "n":
                print("\nThank You for Playing!")
                return None

            else:
                print("Invalid Choice! (Y/N)")


def update_best_time(elapsedTime):
    global bestTime

    if bestTime is None or elapsedTime < bestTime:
        bestTime = elapsedTime
        print("New Best Time!")

    bestMinutes = int(bestTime // 60)
    bestSeconds = int(bestTime % 60)

    print(f"Best Time {bestMinutes}m {bestSeconds}s\n")


def start_game(rows, cols):
    startTime = time.time()
    moveCount = 0

    while True:
        result = player_move(rows, cols)

        if result in ["CONTINUE", "WIN"]:
            moveCount += 1

        if result in ["WIN", "LOSE"]:
            endTime = time.time()

            elapsedTime = endTime - startTime
            minutes = int(elapsedTime // 60)
            seconds = int(elapsedTime % 60)

            print(f"\nMoves Made: {moveCount}")
            print(f"\nTime Elapsed: {minutes}m {seconds}s\n")    

            if result == "WIN":
                update_best_time(elapsedTime)
            break


def check_win(rows, cols):
    for x in range(rows):
        for y in range(cols):
            if board[x][y] != "*" and cloneBoard[x][y] == ".":
                return False
        
    return True


def color_cell(value):
    if value == "*":
        return Fore.RED + "*" + Style.RESET_ALL
    
    elif value == "F":
        return Fore.YELLOW + "F" + Style.RESET_ALL
    
    elif value == ".":
        return Fore.WHITE + "." + Style.RESET_ALL
    
    elif value == 0:
        return " "
    
    else:
        return Fore.CYAN + str(value) + Style.RESET_ALL


def debug_view_board(rows, cols):
    guideRow = list(guide[:rows])
    guideCols = list(guide[:cols])

    print("     " + "   ".join(guideCols))
    print("   +" + "---+" * cols)

    for x in range(rows):
        rowString = f"{guideRow[x]}  |"

        for y in range(cols):
            cell = board[x][y]
            cellDisplay = color_cell(cell)
            rowString += f" {cellDisplay} |"

        print(rowString)
        print("   +" + "---+" * cols)

    print(f"\n{Fore.YELLOW}Flags Remaining: {flagCount}/{totalFlags}{Style.RESET_ALL}\n")


def player_move(rows, cols):
    global flagCount, totalFlags
    while True:
        move = input("Enter the coordinates (e.g., A A to reveal, F A A to flag, U A A to unflag): ").upper().split()

        if debugMode and len(move) == 1 and move[0] == "SHOW":
            print("\nDebug View (Full Board):\n")
            debug_view_board(rows, cols)
            continue
        
        if len(move) == 1 and move[0] == "EXIT":
            print("You gave up! Try Again Next Time!")
            return "LOSE"

        if len(move) not in [2, 3]:
            print("Invalid Coordinates! Please follow the format! A A to reveal, F A A to flag, U A A to unflag!")
            continue

        if len(move) == 3:
            coordinates = list(move)

            if coordinates[1] not in guide[:rows] or coordinates[2] not in guide[:cols]:
                print("Invalid Coordinates!")
                continue  

            coordX = guide.index(coordinates[1]) 
            coordY = guide.index(coordinates[2])

            if coordinates[0] == "F":
                if cloneBoard[coordX][coordY] == ".":
                    if flagCount > 0:
                        cloneBoard[coordX][coordY] = "F"
                        flagCount -= 1

                    else:
                        print("No Flags Remaining!")

                elif cloneBoard[coordX][coordY] == "F":
                    print("Cell Already Flagged!")

                else:
                    print("Cannot Flag this cell!")

            elif coordinates[0] == "U":
                if cloneBoard[coordX][coordY] == "F":
                    cloneBoard[coordX][coordY] = "."
                    flagCount += 1

                else:
                    print("Cell is not Flagged!")

            else:
                print("Invalid Coordinates! Use F or U!")

            print_board(rows, cols)
            return "CONTINUE"

        else:
            coordinates = list(move)

            if coordinates[0] not in guide[:rows] or coordinates[1] not in guide[:cols]:
                print("Invalid Coordinates!")
                continue  

            coordX = guide.index(coordinates[0]) 
            coordY = guide.index(coordinates[1])

            if cloneBoard[coordX][coordY] == "F":
                print("Cell is flagged")
                continue

            if cloneBoard[coordX][coordY] != ".":
                print("Cell is already revealed!")
                continue

            if board[coordX][coordY] == "*":
                for x in range(rows):
                    for y in range(cols):
                        if board[x][y] == "*":
                            cloneBoard[x][y] = "*"

                print_board(rows, cols)
                print("You hit a mine! You lose!")
                return "LOSE"

            else:
                reveal_cell(coordX, coordY, rows, cols)

                if check_win(rows, cols):
                    for x in range(rows):
                        for y in range(cols):
                            if board[x][y] == "*":
                                cloneBoard[x][y] = "*"

                    print_board(rows, cols)
                    print("Congratulations! You've Won the Game!")
                    return "WIN"
                
        print_board(rows, cols)
        return "CONTINUE"


def reveal_cell(coordX, coordY, rows, cols):
    if coordX < 0 or coordX >= rows or coordY < 0 or coordY >= cols:
        return None
    
    if cloneBoard[coordX][coordY] != ".":
        return None
    
    value = board[coordX][coordY]
    cloneBoard[coordX][coordY] = value

    if value == 0:
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x != 0 or y != 0:
                    reveal_cell(x + coordX, y + coordY, rows, cols)


def print_board(rows, cols):
    # Splices the necessary guide letters for rows and cols
    guideRow = list(guide[:rows])
    guideCols = list(guide[:cols])

    # Prints the header guide
    print("     " + "   ".join(guideCols))


    # Prints the board
    print("   +" + "---+" * cols)

    for x in range(rows):
        rowString = f"{guideRow[x]}  |"

        for y in range(cols):
            cell = cloneBoard[x][y]
            cellDisplay = color_cell(cell)
            rowString += f" {cellDisplay} |"

        print(rowString)
        print("   +" + "---+" * cols)

    print(f"\n{Fore.YELLOW}Flags Remaining: {flagCount}/{totalFlags}{Style.RESET_ALL}\n")


def adjust_board(rows, cols):
    # Adds numbers near mines
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "*":
                continue

            bombs = 0

            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    coordX = i + x
                    coordY = j + y

                    if coordX >= 0 and coordX < rows and coordY >= 0 and coordY < cols:
                        if board[coordX][coordY] == "*":
                            bombs += 1
                        
            board[i][j] = bombs

    print_board(rows, cols)



def generate_board(rows, cols, bombsCount):
    # Generates the main board (what players don't see)
    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(0)

        board.append(row)

    # Generates the coordinates
    coordinates = []

    for i in range(rows):
        for j in range(cols):
            coordinates.append((i, j))

    # Uses the generated coordinates to randomly place bombs
    bombPlacement = random.sample(coordinates, bombsCount)

    for x, y in bombPlacement:
        board[x][y] = "*"

    # Generates the clone board (what the players see)
    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(".")

        cloneBoard.append(row)

    adjust_board(rows, cols)


def select_gamemode(choice):
    global flagCount, totalFlags
    if choice == 1:
        rows = 9
        cols = 9
        bombsCount = 9

    elif choice == 2:
        rows = 9
        cols = 9
        bombsCount = 16

    elif choice == 3:
        rows = 9
        cols = 15
        bombsCount = 32

    elif choice == 4:
        rows = 15
        cols = 15
        bombsCount = 54

    else:
        print("Invalid Game Mode!")

        while True:
            print(modeMenu)

            try:
                choice = int(input("Choice: "))

            except ValueError:
                print("Please enter only integer!")
                continue

            select_gamemode(choice)

    flagCount = bombsCount
    totalFlags = bombsCount
    generate_board(rows, cols, bombsCount)
    start_game(rows, cols)


while True:
    print(mainMenu)

    try:
        choice = int(input("Choice: "))

    except ValueError:
        print("Please enter only integer!")
        continue

    if choice == 1:
        main_loop()
        break
    
    elif choice == 2:
        print("Exiting...")
        break

    else:
        print("Invalid Choice! (1-2)")
