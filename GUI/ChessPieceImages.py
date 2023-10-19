import os

# Get the current directory of the chess_images.py module
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the relative file paths for chess piece images in the "assets" directory
piece_image_paths = {
    "BB": os.path.join(current_directory, "..", "assets","BB.png"),
    "BK": os.path.join(current_directory, "..", "assets","BK.png"),
    "BN": os.path.join(current_directory, "..", "assets","BN.png"),
    "BP": os.path.join(current_directory, "..", "assets","BP.png"),
    "BQ": os.path.join(current_directory, "..", "assets","BQ.png"),
    "BR": os.path.join(current_directory, "..", "assets","BR.png"),
    "WB": os.path.join(current_directory, "..", "assets","WB.png"),
    "WK": os.path.join(current_directory, "..", "assets","WK.png"),
    "WN": os.path.join(current_directory, "..", "assets","WN.png"),
    "WP": os.path.join(current_directory, "..", "assets","WP.png"),
    "WQ": os.path.join(current_directory, "..", "assets","WQ.png"),
    "WR": os.path.join(current_directory, "..", "assets","WR.png")
}