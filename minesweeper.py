# Minesweeper - Final Project
# Abat, Arian Dave S.
# Banganan, Grach B.
# 
# Date Created: April 09, 2025
# Current Version: 2.0.04.20.25
# (+) Significantly Improved Overall UI
# (+) Added Main Menu and Settings Menu
# (+) Added Method to toggle Debug Mode
# Lines of code:675
# 
# Current Version: 1.4.04.19.25
# (+) Slightly Improved Overall UI
# (+) Added Method to Always be safe in first move
# (+) Organized the Structure of the Code
# (+) Added New Command
# Lines of code: 500+
# 
# Old Version: 1.3.04.14.25
# (+) Added New Game Difficulty
# (+) Added New Command to Give Up
# Lines of code: 450+
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
# Credits:
# Icon: Minesweeper (Game) - Giant Bomb. (1990, October 8). Giant Bomb. https://www.giantbomb.com/minesweeper/3030-4032/

import random
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def display_welcome_text(terminalWidth):
    welcomeText = [
        "▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .    ▄▄▄▄▄          • ▌ ▄ ·. ▪   ▐ ▄ ▄▄▄ ..▄▄ · ▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄ . ▄▄▄·▄▄▄ .▄▄▄  ",
        "██· █▌▐█▀▄.▀·██•  ▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·    •██  ▪         ·██ ▐███▪██ •█▌▐█▀▄.▀·▐█ ▀. ██· █▌▐█▀▄.▀·▀▄.▀·▐█ ▄█▀▄.▀·▀▄ █·",
        "██▪▐█▐▐▌▐▀▀▪▄██▪  ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▐█.▪ ▄█▀▄     ▐█ ▌▐▌▐█·▐█·▐█▐▐▌▐▀▀▪▄▄▀▀▀█▄██▪▐█▐▐▌▐▀▀▪▄▐▀▀▪▄ ██▀·▐▀▀▪▄▐▀▀▄ ",
        "▐█▌██▐█▌▐█▄▄▌▐█▌▐▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌     ▐█▌·▐█▌.▐▌    ██ ██▌▐█▌▐█▌██▐█▌▐█▄▄▌▐█▄▪▐█▐█▌██▐█▌▐█▄▄▌▐█▄▄▌▐█▪·•▐█▄▄▌▐█•█▌",
        " ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀      ▀▀▀  ▀█▄▀▪    ▀▀  █▪▀▀▀▀▀▀▀▀ █▪ ▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▪ ▀▀▀  ▀▀▀ .▀    ▀▀▀ .▀  ▀"
    ]
    
    for line in welcomeText:
        print(f"{Fore.MAGENTA + Style.BRIGHT}{line.center(terminalWidth)}")
        time.sleep(0.1)

    print()

    time.sleep(0.5)


def display_win(terminalWidth):
    victoryText = [
        "██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗",
        "╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║",
        " ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║",
        "  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║",
        "   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║",
        "   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝"
    ]

    for line in victoryText:
        print(f"{Fore.GREEN + Style.BRIGHT}{line.center(terminalWidth)}")
        time.sleep(0.1)

    print()


def display_lose(terminalWidth):
    loseText = [
        "██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗",
        "╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝",
        " ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ",
        "  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ",
        "   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗",
        "   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝"
    ] 

    for line in loseText:
        print(f"{Fore.RED + Style.BRIGHT}{line.center(terminalWidth)}")
        time.sleep(0.1)

    print()


def display_gave_up(terminalWidth):
    gaveUpText = [
        "██╗   ██╗ ██████╗ ██╗   ██╗     ██████╗  █████╗ ██╗   ██╗███████╗    ██╗   ██╗██████╗ ",
        "╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝ ██╔══██╗██║   ██║██╔════╝    ██║   ██║██╔══██╗",
        " ╚████╔╝ ██║   ██║██║   ██║    ██║  ███╗███████║██║   ██║█████╗      ██║   ██║██████╔╝",
        "  ╚██╔╝  ██║   ██║██║   ██║    ██║   ██║██╔══██║╚██╗ ██╔╝██╔══╝      ██║   ██║██╔═══╝ ",
        "   ██║   ╚██████╔╝╚██████╔╝    ╚██████╔╝██║  ██║ ╚████╔╝ ███████╗    ╚██████╔╝██║     ",
        "   ╚═╝    ╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝     ╚═════╝ ╚═╝     "
    ] 

    for line in gaveUpText:
        print(f"{Fore.LIGHTYELLOW_EX + Style.BRIGHT}{line.center(terminalWidth)}")
        time.sleep(0.1)

    print()


def display_exit(terminalWidth):
    exitText = [
        " ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗",
        "██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║",
        "██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║",
        "██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝",
        "╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗",
        " ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝"
    ]

    print()

    for line in exitText:
        print(f"{Fore.MAGENTA + Style.BRIGHT}{line.center(terminalWidth)}")
        time.sleep(0.1)


def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    
    except:
        return 80
    
    
def calculate_padding(x, y):
    return (x - y) // 2


def display_stats(elapsedTime, totalMoves, terminalWidth):
    statsHeader = "📈 YOUR TOTAL STATISTICS 📈"
    print(f"\n{Fore.LIGHTYELLOW_EX + Style.BRIGHT}{statsHeader.center(terminalWidth)}")

    statsItems = [
        f"Total Time: {elapsedTime // 60}m {elapsedTime % 60}s",
        f"Total Moves: {totalMoves}\n"
    ]

    maxLength = 0

    for length in statsItems: 
        if len(length) > maxLength:
            maxLength = len(length)


    paddingStr = " " * calculate_padding(terminalWidth, maxLength)

    for item in statsItems:
        print(f"{paddingStr}{Fore.LIGHTYELLOW_EX + Style.BRIGHT}{item}")
        time.sleep(0.1)
    

def display_help(terminalWidth):
    menuHeader = "📜 COMMANDS 📜"
    print(f"\n{Fore.CYAN + Style.BRIGHT}{menuHeader.center(terminalWidth)}")

    menuItems = [
        "A A         - Reveal Cell",
        "F A A       - Flag Cell",
        "U A A       - Unflag Cell",
        "SHOW        - Show Full Board (Debug Mode)",
        "EXIT        - Give Up",
        "HELP        - Show Commands\n",
    ]
    
    maxLength = 0

    for length in menuItems:
        if len(length) > maxLength:
            maxLength = len(length)


    paddingStr = " " * calculate_padding(terminalWidth, maxLength)

    for item in menuItems:
        print(f"{Fore.CYAN}{paddingStr}{item}")
        time.sleep(0.1)


def display_settings_menu(terminalWidth, debugMode):
    menuHeader = "⚙️ SETTINGS MENU ⚙️"
    print(f"\n{Fore.GREEN + Style.BRIGHT}{menuHeader.center(terminalWidth)}")

    if debugMode:
        debugStatus = "ON"

    else:
        debugStatus = "OFF"

    menuItems = [
        f"{Fore.CYAN}[1] Debug Mode: {Fore.YELLOW + Style.BRIGHT}{debugStatus}{Style.RESET_ALL}",
        f"{Fore.CYAN}[2] Return to Main Menu\n"
    ]

    maxLength = 0

    for item in menuItems:
        if len(item) > maxLength:
            maxLength = len(item)

    paddingStr = " " * calculate_padding(terminalWidth, maxLength)

    for item in menuItems:
        print(f"{paddingStr}{item}")
        time.sleep(0.1)

    choice = input(f"{Fore.YELLOW}Select Option (1-2): ")
    
    return choice


def display_difficulty_menu(terminalWidth):
    menuHeader = "💣 SELECT DIFFICULTY LEVEL 💣"
    print(f"\n{Fore.RED + Style.BRIGHT}{menuHeader.center(terminalWidth)}")

    menuItems = [
        "[1] Easy",
        "[2] Medium",
        "[3] Hard",
        "[4] Very Hard",
        "[5] Return to Main Menu\n"
    ]

    maxLength = 0

    for item in menuItems:
        if len(item) > maxLength:
            maxLength = len(item)

    paddingStr = " " * calculate_padding(terminalWidth, maxLength)

    for item in menuItems:
        print(f"{Fore.CYAN}{paddingStr}{item}")
        time.sleep(0.1)

    choice = input(f"{Fore.YELLOW}Select Difficulty (1-5): ")

    return choice


def display_main_menu(terminalWidth):
    menuHeader = "🎮 MAIN MENU 🎮"
    print(f"\n{Fore.BLUE + Style.BRIGHT}{menuHeader.center(terminalWidth)}\n")

    menuItems = [
        "[1] Play Game",
        "[2] Settings",
        "[3] Exit\n"
    ]

    maxLength = 0

    for item in menuItems:
        if len(item) > maxLength:
            maxLength = len(item)

    paddingStr = " " * calculate_padding(terminalWidth, maxLength)

    for item in menuItems:
        print(f"{Fore.CYAN}{paddingStr}{item}")
        time.sleep(0.1)

    choice = input(f"{Fore.YELLOW}Select Option (1-3): ")
    
    return choice


class Minesweeper:
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombsCount = bombs
        self.flagCount = bombs
        self.totalFlags = bombs
        self.board = []
        self.cloneBoard = []
        self.debugMode = True
        self.first_move_done = False
        self.bestTime = None
        self.boardWidth = 4 + (self.cols * 4)
        self.terminalWidth = get_terminal_width()
        self.generate_boards()


    def generate_boards(self, safe_coords=None):
        self.board = []
        self.cloneBoard = []
        coordinates = []

        for x in range(self.rows):
            row = []
            cloneRow = []
            
            for y in range(self.cols):
                row.append(0)
                cloneRow.append(".")
                coordinates.append((x, y))

            self.board.append(row)
            self.cloneBoard.append(cloneRow)

        if safe_coords is not None:
            safeCoordX = safe_coords[0]
            safeCoordY = safe_coords[1]

            safeCoordinates = []

            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    coordX = safeCoordX + x
                    coordY = safeCoordY + y

                    if 0 <= coordX < self.rows and 0 <= coordY < self.cols:
                        safeCoordinates.append((coordX, coordY))

            filteredCoordinates = []
            for coord in coordinates:
                if coord not in safeCoordinates:
                    filteredCoordinates.append(coord)

            coordinates = filteredCoordinates

            bombPlacement = random.sample(coordinates, self.bombsCount)

            for x, y in bombPlacement:
                self.board[x][y] = "*"

        self.adjust_board()


    def adjust_board(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.board[x][y] == "*":
                    continue

                bombs = 0

                for xx in [-1, 0, 1]:
                    for yy in [-1, 0, 1]:
                        coordX = x + xx
                        coordY = y + yy
                        
                        if 0 <= coordX < self.rows and 0 <= coordY < self.cols:
                            if self.board[coordX][coordY] == "*":
                                bombs += 1

                self.board[x][y] = bombs


    def get_guide(self, length):
        return list("ABCDEFGHIJKLMNO"[:length])
    

    def color_cell(self, value):
        colorMap = [Fore.BLUE, Fore.GREEN, Fore.RED, Fore.BLACK, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

        if value == "*":
            return Fore.RED + Style.BRIGHT + "*" + Style.RESET_ALL
        
        elif value == "F":
            return Fore.YELLOW + Style.BRIGHT + "F" + Style.RESET_ALL
        
        elif value == ".":
            return Fore.WHITE + Style.BRIGHT +"."
        
        elif value == 0:
            return " "
        
        else:
            return colorMap[value - 1] + Style.BRIGHT + str(value) + Style.RESET_ALL


    def print_board(self, reveal=False):
        guideRow = self.get_guide(self.rows)
        guideCols = self.get_guide(self.cols)

        paddingStr = " " * calculate_padding(self.terminalWidth, self.boardWidth)

        print(paddingStr + "     " + "   ".join(guideCols))
        print(paddingStr + "   ┌" + "───┬" * (self.cols - 1) + "───┐")

        for x in range(self.rows):
            print(f"{paddingStr}{guideRow[x]}  │", end=" ")

            for y in range(self.cols):
                if reveal:
                    cell = self.board[x][y]

                else:
                    cell = self.cloneBoard[x][y]

                cellDisplay = self.color_cell(cell)

                print(f"{cellDisplay} │", end=" ")
            
            if x < self.rows - 1:
                print("\n" + paddingStr + "   ├" + "───┼" * (self.cols - 1) + "───┤")

        print("\n" + paddingStr + "   └" + "───┴" * (self.cols - 1) + "───┘")

        print(f"\n{Fore.YELLOW}Flags Remaining: {self.flagCount}/{self.totalFlags}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Legend: {Fore.RESET}. = Hidden, {Fore.YELLOW}F{Fore.RESET} = Flag, {Fore.RED}*{Fore.RESET} = Bomb, {Fore.MAGENTA}[1–8]{Fore.RESET} = Nearby Bombs\n")


    def print_help(self):
        display_help(self.terminalWidth)

    def start_game(self):
        startTime = time.time()
        moves = 0

        while True:
            self.print_board()

            moves += 1         
            result = self.player_move()

            elapsedTime = int(time.time() - startTime)
            print(f"{Fore.LIGHTYELLOW_EX}Move #{moves} | Time Elapsed: {elapsedTime // 60}m {elapsedTime % 60}s\n")

            if result == "HELP":
                display_help(self.terminalWidth)
                continue

            if result == "EXIT":
                display_gave_up(self.terminalWidth)
                break

            if result in ["WIN", "LOSE"]:
                self.print_board(reveal=True)

                display_stats(elapsedTime, moves, self.terminalWidth)

                if result == "WIN":
                    if self.bestTime is None or elapsedTime < self.bestTime:
                        self.bestTime = elapsedTime
                        text = f"{Fore.LIGHTYELLOW_EX + Style.BRIGHT}🎊 NEW BEST TIME! 🎊"
                        padding = " " * calculate_padding(self.terminalWidth, len(text))
                        print(f"\n{padding}{text}\n")

                    display_win(self.terminalWidth)

                else:
                    display_lose(self.terminalWidth)

                break
   

    def player_move(self):
        move = input("Enter the coordinates (e.g., A A to reveal, F A A to flag, U A A to unflag): ").upper().split()
        print()

        if len(move) == 1:
            if self.debugMode and move[0] == "SHOW":
                headerText = f"{Fore.MAGENTA + Style.BRIGHT}{Style.NORMAL} (FULL BOARD):"
                padding = " " * calculate_padding(self.terminalWidth, len(headerText))
                print(f"\n{padding}{headerText}\n")
                self.print_board(reveal=True)
                return "CONTINUE"
        
            elif move[0] == "HELP":
                return "HELP"
        
        if len(move) == 1 and move[0] == "EXIT":
            return "EXIT"
        
        if len(move) == 3 and move[0] in ["F", "U"]:
            action, x, y = move
            return self.handle_flags(action, x ,y)
        
        if len(move) == 2:
            x, y = move
            return self.reveal_cell(x, y)
        
        print(f"{Fore.RED}{Style.BRIGHT}INVALID{Style.NORMAL} Input\n")
        return "CONTINUE"
        

    def handle_flags(self, action, x, y):
        if x not in self.get_guide(self.rows) or y not in self.get_guide(self.cols):
            print(f"{Fore.RED}{Style.BRIGHT}INVALID{Style.NORMAL} Coordinates!\n")
            return "CONTINUE"
        
        coordX = self.get_guide(self.rows).index(x)
        coordY = self.get_guide(self.cols).index(y)

        if action == "F":
            if self.cloneBoard[coordX][coordY] == "." and self.flagCount > 0:
                self.cloneBoard[coordX][coordY] = "F"
                self.flagCount -= 1

            elif self.cloneBoard[coordX][coordY] == "F":
                print(f"{Fore.RED}Cell is already {Style.BRIGHT}FLAGGED!\n")

            else:
                print(f"{Fore.RED + Style.BRIGHT}CANNOT{Style.NORMAL} Flag this Cell!\n")

        elif action == "U":
            if self.cloneBoard[coordX][coordY] == "F":
                self.cloneBoard[coordX][coordY] = "."
                self.flagCount += 1

            else:
                print(f"{Fore.RED}Cell is not {Style.BRIGHT}FLAGGED!\n")

        return "CONTINUE"
    

    def reveal_cell(self, x, y):
        if x not in self.get_guide(self.rows) or y not in self.get_guide(self.cols):
            print(f"{Fore.RED + Style.BRIGHT}INVALID{Style.NORMAL} Coordinates!\n")
            return "CONTINUE"
        
        coordX = self.get_guide(self.rows).index(x)
        coordY = self.get_guide(self.cols).index(y)

        if self.cloneBoard[coordX][coordY] == "F":
            print(f"{Fore.RED}Cell is {Style.BRIGHT}FLAGGED!\n")
            return "CONTINUE"
        
        if not self.first_move_done:
            self.generate_boards(safe_coords=[coordX, coordY])
            self.first_move_done = True
        
        if self.board[coordX][coordY] == "*":
            self.cloneBoard[coordX][coordY] = "*"
            return "LOSE"
        
        if self.cloneBoard[coordX][coordY] != ".":
            print(f"{Fore.RED}Cell is {Style.BRIGHT}ALREADY REVEALED!\n")
            return "CONTINUE"


        self.reveal_neighbors(coordX, coordY)
        
        if self.check_win():
            return "WIN"
        
        return "CONTINUE"
        

    def reveal_neighbors(self, coordX , coordY):
        if not (0 <= coordX < self.rows and 0 <= coordY < self.cols):
            return None
        
        if self.cloneBoard[coordX][coordY] != ".":
            return None
        
        self.cloneBoard[coordX][coordY] = self.board[coordX][coordY]

        if self.board[coordX][coordY] == 0:
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x != 0 or y != 0:
                        self.reveal_neighbors((coordX + x), (coordY + y))


    def check_win(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.board[x][y] != "*" and self.cloneBoard[x][y] == ".":
                    return False
                
        return True
    

def main_menu():
    terminalWidth = get_terminal_width()
    debugMode = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_welcome_text(terminalWidth)
        choice = display_main_menu(terminalWidth)
        
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            display_welcome_text(terminalWidth)
                
            difficulty = display_difficulty_menu(terminalWidth)
                
            levels = {
                "1": (9, 9, 9),
                "2": (9, 9, 16),
                "3": (9, 15, 32),
                "4": (15, 15, 54),
                "5": None
            }

            if difficulty == "5":
                continue

            if difficulty not in levels:
                print(f"{Fore.RED + Style.BRIGHT}INVALID{Style.RESET_ALL} choice")
                time.sleep(0.5)
                continue

            rows, cols, bombs = levels[difficulty]
            game = Minesweeper(rows, cols, bombs)
            game.debugMode = debugMode
            
            os.system('cls' if os.name == 'nt' else 'clear')
            game.start_game()
            
            input(f"\n{Fore.YELLOW}Press Any Key to return to main menu...{Style.RESET_ALL}")
                
        elif choice == "2":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                display_welcome_text(terminalWidth)
                settings_choice = display_settings_menu(terminalWidth, debugMode)
                
                if settings_choice == "1":
                    debugMode = not debugMode
                    status = "ON" if debugMode else "OFF"
                    print(f"\n{Fore.GREEN}Debug mode is now {Fore.YELLOW + Style.BRIGHT}{status}{Style.RESET_ALL}")
                    time.sleep(0.5)
                    
                elif settings_choice == "2":
                    break
                    
                else:
                    print(f"{Fore.RED + Style.BRIGHT}INVALID{Style.NORMAL} choice")
                    time.sleep(0.5)
                
        elif choice == "3":
            display_exit(terminalWidth)
            break
            
        else:
            print(f"{Fore.RED + Style.BRIGHT}INVALID{Style.NORMAL}x choice")
            time.sleep(0.5)

    
def main():
    main_menu()

if __name__ == "__main__":
    main()