from main_AI import TicTacToe
import tkinter as tk
from tkinter import ttk
import sv_ttk


# Define the TicTacToeGUI class
class TicTacToeGUI:
    def __init__(self, thegame):
        self.game = thegame
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Set the minimum and maximum window size
        self.window.minsize(600, 600)  # Set the minimum width and height of the window
        self.window.maxsize(1200, 1200)  # Set the maximum width and height of the window

        # Configure rows and columns to expand and fill available space
        for i in range(3):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

        # Create the buttons grid for the Tic Tac Toe board
        self.buttons = [[tk.Button(self.window, text="", font='Arial 60', width=2,
                                   command=lambda row=i, col=j: self.click_buttons(row, col))
                         for j in range(3)] for i in range(3)]

        # Place the buttons in the window using grid layout and sticky option for filling the available space
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, sticky="nsew")

        sv_ttk.set_theme("dark")  # Set the theme to "dark"

        # Create the result label for displaying game outcomes
        self.result_label = tk.Label(self.window, text="", font='Arial 25')

        # Place the result label below the Tic Tac Toe board
        self.result_label.grid(row=3, column=0, columnspan=3)

        # Create the reset button for restarting the game
        self.reset_button = ttk.Button(
            self.window, text="Reset", command=self.reset_game, width=10)

        # Place the reset button below the result label with padding
        self.reset_button.grid(row=4, column=1, pady=100)

        # Configure additional rows and columns to expand
        self.window.grid_rowconfigure(4, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)

        self.result_shown = False  # Flag to indicate if the result is shown

    def click_buttons(self, i, j):
        # Check if the result is not shown and the clicked cell is empty
        if not self.result_shown and self.game[i, j] == self.game.FREE_CELL:
            self.game[i, j] = self.game.HUMAN_X  # Set the value of the clicked cell to HUMAN_X
            self.buttons[i][j]["text"] = "X"  # Update the button text to display "X"
            # Check if the human player has won
            if self.game.is_human_win:
                self.display_result("You won!")
                # Get the winning cells
                winning_cells = self.game.get_winning_cells(self.game.HUMAN_X)
                # Update the button color for the winning cells
                for cell in winning_cells:
                    cell_row, cell_col = cell
                    self.buttons[cell_row][cell_col]["bg"] = "green"
            # Check if it's a draw
            elif self.game.is_draw:
                self.display_result("It's a draw.")
            else:
                self.computer_turn()  # Proceed with the computer's turn
        else:
            print('The cell is not empty')

    def computer_turn(self):
        self.game.computer_go()  # Perform the computer's turn
        for i in range(3):
            for j in range(3):
                # Update the buttons text to display "O" for computer's moves
                if self.game[i, j] == self.game.COMPUTER_O:
                    self.buttons[i][j]["text"] = "O"
        # Check if the computer player has won
        if self.game.is_computer_win:
            self.display_result("You lost.")
            # Get the winning cells
            winning_cells = self.game.get_winning_cells(self.game.COMPUTER_O)
            # Update the button color for the winning cells
            for cell in winning_cells:
                cell_row, cell_col = cell
                self.buttons[cell_row][cell_col]["bg"] = "red"
        # Check if it's a draw
        elif self.game.is_draw:
            self.display_result("It's a draw.")

    def reset_button_color(self):
        # Reset the background color of all buttons to default
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["bg"] = self.window.cget('bg')

    def display_result(self, message):
        # Update the text of the result label to display the game outcome message
        self.result_label["text"] = message
        self.result_shown = True  # Set the flag to indicate that the result is shown
        self.disable_buttons()  # Disable the buttons to prevent further moves

    def disable_buttons(self):
        # Disable all buttons in the grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["state"] = tk.DISABLED

    def run(self):
        self.window.mainloop()

    def reset_game(self):
        # Reset the game state and clear the button text
        self.game.reset()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = tk.NORMAL  # Enable the buttons for a new game
        self.result_label["text"] = ""  # Clear the result label
        self.result_shown = False  # Reset the flag to indicate that the result is not shown
        self.reset_button_color()  # Reset the button colors


# Create a TicTacToe object and initialize the game
game = TicTacToe()
game.init()

# Create a TicTacToeGUI object with the game and run the GUI application
gui = TicTacToeGUI(game)
gui.run()