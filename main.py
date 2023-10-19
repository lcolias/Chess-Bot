import sys
from GUI.ChessGui import ChessGUI
import tkinter as tk

__small_board = 64
__large_board = 96

def main():

    # Access command-line arguments
    arguments = sys.argv[1:]  # Slice to remove the script name


    # Check if we're running simulations or if we're playing against the bot
    for arg in arguments:
        
        if arg == '-play':
            break
        elif arg == '-sim':
            break 
   
    root = tk.Tk()

    root.wm_attributes('-transparentcolor', 'grey')

    chessGUI = ChessGUI(root, __small_board)
    root.mainloop()

if __name__ == '__main__':
    main()