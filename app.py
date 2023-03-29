from tkinter import *
import main_gui

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("FURNITURE STORE MANAGEMENT SYSTEM")
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry("{width}x{height}+0+0".format(width=self.width, height=self.height))
        self.state("zoomed")
        main_gui.FurnitureStore(self)

if __name__ == "__main__":
    g=GUI()
    g.mainloop()
    
