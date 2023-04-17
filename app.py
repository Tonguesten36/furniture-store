from tkinter import *
import main_gui

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("FURNITURE STORE MANAGEMENT SYSTEM")
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry("{width}x{height}+0+0".format(width=self.width, height=self.height))
        
        # This one only works on Windows,
        #  if you want to run this on Linux or Mac, then change it to normal
        self.state("zoomed")
        
        main_gui.FurnitureStore(self)

# Driver code
if __name__ == "__main__":
    g=GUI()
    g.mainloop()
    
