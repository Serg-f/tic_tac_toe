# tic_tac_toe study project
 
- minimax algorithm - [Learn How to Lose the Game](https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f) 
- [tkinker](https://realpython.com/python-gui-tkinter/) GUI with [ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme/tree/main)
- run game_GUI.py
- just lose or draw, the AI is invincible :)

<img src="/screenshot.png" alt="scrn" width="500" height="700">

# main_AI.py
This code provides a basic implementation of the Tic-Tac-Toe game logic and is expanded upon for user interaction with tkinker GUI.
- Cell class: Represents a cell in the Tic-Tac-Toe game board. It has an initial value of 0 and overrides the __bool__ method to return True if the cell value is not 0.
- TicTacToe class: Represents the game itself. It has constants defined for various cell values and display characters. The game board is represented as a 3x3 grid of Cell objects.
- __getitem__ and __setitem__ methods: Allow accessing and updating the cell values in the game board using indexing syntax.
- init method: Initializes the game board by setting all cell values to the free cell value.
- show method: Displays the current state of the game board.
- reset method: Resets the game by calling the init method to clear the board.
- computer_go method: Implements the computer player's move using the minimax algorithm to find the best move.
- minimax method: Implements the minimax algorithm to determine the best move for the computer player.
- _is_win method: Checks if there is a row, column, or diagonal in the game board with a specified cell value.
- is_human_win, is_computer_win, and is_draw properties: Check if a player has won or if the game is a draw.
- __bool__ method: Checks if the game is over by evaluating the winning conditions.
- get_winning_cells method: Retrieves the coordinates of the winning cells for a given player.
- game instance: Creates an instance of the TicTacToe class and initializes the game board.
- step_game variable: Represents the current step or turn in the game.

# game_GUI.py
This code combines the game logic of Tic-Tac-Toe with a graphical user interface, allowing players to play the game by clicking on the GUI buttons and see the game outcomes visually.
- The TicTacToeGUI class represents the GUI for the game. It initializes a window using tkinter and sets its title.
- The GUI window is configured with a minimum and maximum size, and rows and columns are configured to expand and fill the available space.
- The Tic-Tac-Toe board is represented by a grid of buttons created using the tk.Button class. Each button corresponds to a cell in the game board.
- The sv_ttk.set_theme("dark") line sets the theme of the GUI to "dark" using the sv_ttk library.
- A result label is created to display the game outcomes, such as the winner or a draw.
- A reset button is created to restart the game. When clicked, it calls the reset_game method.
- The buttons, result label, and reset button are placed in the window using the grid layout.
- The click_buttons method handles the button clicks by the human player. It updates the game state, button text, and checks for a win or draw.
- The computer_turn method performs the computer player's turn by making a move using the game.computer_go method. It updates the button text and checks for a win or draw.
- Various helper methods are included to update button colors, display the game result, disable buttons, and reset the game.
- The run method starts the GUI main event loop to handle user interactions and updates.
- An instance of the TicTacToe class is created and initialized to represent the game logic.
- An instance of the TicTacToeGUI class is created with the game instance, and the GUI application is run.
