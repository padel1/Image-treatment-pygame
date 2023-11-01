from tkinter import filedialog
from tkinter import Tk


class Helper:
    def __init__(self) -> None:
        pass

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tif")],
        )
        return file_path  # Return the file path

    def initialize_root(self):
        root = Tk()
        root.withdraw()
        return root
