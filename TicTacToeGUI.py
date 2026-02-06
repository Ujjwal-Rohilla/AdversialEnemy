import tkinter as tk
import XO_Ai as ai

buttons = []
current_player = "X"

def initGUI(board, isAI=False):
    gui = tk.Tk()
    gui.geometry("600x600")
    gui.title("Tic Tac Toe")
    
    # Label to display the game result
    result_label = tk.Label(master=gui, text="")
    result_label.pack()

    # Tic-tac-toe grid
    middle_frame = tk.Frame(master=gui)
    middle_frame.pack(fill=tk.BOTH, expand=True)

    for i in range(3):
        middle_frame.columnconfigure(i, weight=1, minsize=50)
        middle_frame.rowconfigure(i, weight=1, minsize=50)

    # 3x3 Grid of Buttons
    for i in range(3):
        row = []
        for j in range(3):
            if isAI:
                button = tk.Button(master=middle_frame, text="", height=2, width=5, relief="ridge", bd=3,
                                command=lambda i=i, j=j: handle_click(i, j, board, gui, result_label, True))
            elif isAI == False:
                button = tk.Button(master=middle_frame, text="", height=2, width=5, relief="ridge", bd=3,
                               command=lambda i=i, j=j: handle_click(i, j, board, gui, result_label))
            button.grid(row=i, column=j, sticky="nsew")
            row.append(button)
        buttons.append(row)

    
    def on_closing():
        exit()

    gui.protocol("WM_DELETE_WINDOW", on_closing)

    gui.mainloop()

def handle_click(i, j, board, gui ,result_label, isAI=False):
    global current_player  
    
    # Get the current button
    button = buttons[i][j]

    # Update the button's text and the board if the button is empty
    if button["text"] == "":
        button["text"] = current_player  # Player's move
        board[i][j] = button["text"]
        
        # Switch the current player's symbol
        if not isAI:  # Only switch the player's symbol in a PvP game
            current_player = "O" if current_player == "X" else "X"

        # Check if the game is over after the player's move
        if ai.terminal(board):
            # Update the label's text with the game result
            if ai.check_win("X", board):
                result_label["text"] = "X Won!"
            elif ai.check_win("O", board):
                result_label["text"] = "O Won!"
            else:
                result_label["text"] = "Draw!"

            # Disable all buttons
            for row in buttons:
                for button in row:
                    button.config(state=tk.DISABLED)
            return

        if isAI:
            # AI's move
            result_label["text"] = "AI's Turn"
            gui.update()  # Update the GUI to show the label's new text

            ai_move = ai.minimax(board)  # Get the AI's move
            if ai_move is not None:
                buttons[ai_move[0]][ai_move[1]]["text"] = "O"  # Update the button's text
                board[ai_move[0]][ai_move[1]] = "O"  # Update the board

        # Check if the game is over after the AI's move
        if ai.terminal(board):
            # Update the label's text with the game result
            if ai.check_win("X", board):
                result_label["text"] = "X Won!"
            elif ai.check_win("O", board):
                result_label["text"] = "O Won!"
            else:
                result_label["text"] = "Draw!"

            # Disable all buttons
            for row in buttons:
                for button in row:
                    button.config(state=tk.DISABLED)
        
        else:
            if isAI:
                result_label["text"] = "Your Turn"
            elif isAI == False:
                result_label["text"] = "X's Turn" if current_player == "X" else "O's Turn"