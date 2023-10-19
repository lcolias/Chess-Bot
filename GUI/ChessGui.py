from tkinter import *
from PIL import Image, ImageTk

from GUI.ChessPieceImages import piece_image_paths
from GUI.MenuCommands import *

__MAGIC_NUMBER__ = 8

class ChessGUI:

    
    __board = None
    __piece_images = {}
    __piece_labels = {}

    # Initialize the Chess Board GUI  
    def __init__(self, root, boardsize): 
        self.root = root
        self.boardsize = boardsize
        self.root.title("Chess Bot")
        
        self.create_menu()
        self.create_chessboard()
        self.init_pieces()

    # Creates the menu opjects for the GUI
    def create_menu(self):

        # Create menubar object
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        # Create File menu object
        file_menu = Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)

        # Add File menu commands: New Game, Save Game, Exit
        file_menu.add_command(label="New Game", command=self.new_game)
        file_menu.add_command(label="Save Game", command=self.save_game)
        file_menu.add_command(label="Load Game", command=self.load_game)
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Create Simulation menu object
        simulation_menu = Menu(menubar)
        menubar.add_cascade(label="Simulation", menu=simulation_menu)
        
        # Add Simulation menu commands: New Game, Save Game, Exit
        simulation_menu.add_command(label="GM Simulation", command=self.sim_GM)
        simulation_menu.add_command(label="Bot Simulation", command=self.sim_Bot)

    # Creates the chessboard grid
    def create_chessboard(self):

        # Create labels to display column headers (letters 'a' to 'h') on the bottom side
        for j in range(__MAGIC_NUMBER__):
            header_label = Label(self.root, text=chr(ord('a') + j))
            header_label.grid(row=8, column=j+1)

        # Create labels to display row headers (numbers '1' to '8') on the left side
        for i in range(__MAGIC_NUMBER__):
            header_label = Label(self.root, text=str(__MAGIC_NUMBER__ - i))
            header_label.grid(row=i, column=0)

        # Create a Canvas object with an 8x8 grid of rectabgles to represent the chessboard
        # The canvas is sized by the main function passing a size variable
        self.__board = Canvas(self.root, width=self.boardsize * __MAGIC_NUMBER__, height=self.boardsize * __MAGIC_NUMBER__)

        square_size = self.boardsize
        colors = ["white", "black"]
        for row in range(__MAGIC_NUMBER__):
            for col in range(__MAGIC_NUMBER__):
                x1, y1 = col * square_size, row * square_size
                x2, y2 = x1 + square_size, y1 + square_size
                self.__board.create_rectangle(x1, y1, x2, y2, fill=colors[(row + col) % 2], outline=colors[(row + col) % 2])

        self.__board.grid(row=0, column=1, rowspan=__MAGIC_NUMBER__, columnspan=__MAGIC_NUMBER__)

       

     # Creates the chessboard grid
    def init_pieces(self):

       
        # Load chess piece images using the PhotoImage constructor
        # Load, resize, and display chess piece images using Pillow
        for piece in piece_image_paths:
            image = Image.open(piece_image_paths[piece]).convert('RGBA')
            image = image.resize((self.boardsize, self.boardsize))
            self.__piece_images[piece] = ImageTk.PhotoImage(image)
        
        # Convert the images to PhotoImage objects and create labels
        for row in range(__MAGIC_NUMBER__):
            
            if (row <= 1 or row >= 6):

                for col in range(__MAGIC_NUMBER__):

                    piece = self.get_chess_piece_for_pos(row, col)
                    
                    colors = ["white", "black"]
                    label = Label(self.__board, image=self.__piece_images.get(piece), bg=colors[(row + col) % 2])

                    self.__piece_labels[(row, col)] = label
                 
                    label.lift()

                    x = col * self.boardsize
                    y = row * self.boardsize
                    label.place(x=x, y=y)

                    

    def get_chess_piece_for_pos(self, row, col):
        if row == 0:
            if col == 0 or col == 7:
                return "BR"
            elif col == 1 or col == 6:
                return "BN"
            elif col == 2 or col == 5:
                return "BB"
            elif col == 3:
                return "BQ"
            elif col == 4:
                return "BK"
            else:
                return "Invalid Pos(col)"
        elif row == 1:
            return "BP"
        elif row == 6:
            return "WP"
        elif row == 7:
            if col == 0 or col == 7:
                return "WR"
            elif col == 1 or col == 6:
                return "WN"
            elif col == 2 or col == 5:
                return "WB"
            elif col == 3:
                return "WQ"
            elif col == 4:
                return "WK"
            else:
                return "Invalid Pos(col)"
        else:
            print (row)
            return "Invalid Pos(row)"
       

    def new_game(self):
        print("New Game")
    

    def save_game(self):
        print("Save Game")
        

    def load_game(self):
        print("Load Game")
        

    def sim_GM(self):
        print("Sim GM")
        

    def sim_Bot(self):
        print("Sim Bot")