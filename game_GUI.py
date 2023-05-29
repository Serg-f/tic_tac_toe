from main_AI import TicTacToe, Cell, run_game_in_terminal
import tkinter as tk

class TicTacToeGUI:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = [[tk.Button(self.window, text="_", font='Arial 60', width=2,
                                   command=lambda row=i, col=j: self.click_buttons(row, col))
                         for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

        self.result_label = tk.Label(self.window, text="", font='Arial 20')  # label for game result
        self.result_label.grid(row=4, column=0, columnspan=3)  # place it under the game board

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=5, column=1)

    def click_buttons(self, i, j):
        if self.game[i, j] == self.game.FREE_CELL:
            self.game[i, j] = self.game.HUMAN_X
            self.buttons[i][j]["text"] = "X"
            if self.game.is_human_win:
                self.display_result("You won!")
            elif self.game.is_draw:
                self.display_result("It's a draw.")
            else:
                self.computer_turn()
        else:
            print('The cell is not empty')

    def computer_turn(self):
        self.game.computer_go()
        for i in range(3):
            for j in range(3):
                if self.game[i, j] == self.game.COMPUTER_O:
                    self.buttons[i][j]["text"] = "O"
        if self.game.is_computer_win:
            self.display_result("You lost.")
        elif self.game.is_draw:
            self.display_result("It's a draw.")

    def display_result(self, message):
        self.result_label["text"] = message  # update the text of the result label

    def run(self):
        self.window.mainloop()

    def reset_game(self):
        self.game.reset()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = "_"
        self.result_label["text"] = ""  # clear the result label

game = TicTacToe()
game.init()
gui = TicTacToeGUI(game)
gui.run()
