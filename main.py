from calendar import c
import sys
from GUI.ChessGui import ChessGUI
import tkinter as tk
import chess
__small_board = 64
__large_board = 96

def main():

    # Access command-line arguments
    arguments = sys.argv[1:]  # Slice to remove the script name


    # Check if we're running simulations or if we're playing against the bot
    for arg in arguments:
        
        if arg == '-play':
            break
            break 
   
    board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")

    chess.svg.piece(chess.Piece.from_symbol("R"))
    
    # Create tkinter root object 
    #root = tk.Tk()
    # root.wm_attributes('-transparentcolor', 'grey') 
    #chessGUI = ChessGUI(root, __small_board)
    #root.mainloop()

if __name__ == '__main__':
    main()