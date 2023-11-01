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

    def widget_visibility(self, widget, show_list):
        for i in widget:
            if i in show_list:
                i.show()
            else:
                i.hide()
