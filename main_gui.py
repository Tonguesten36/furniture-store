from tkinter import *
from PIL import ImageTk, Image
from windows import fun1, fun2, fun3, fun4
import os, pathlib

class FurnitureStore:
    def __init__(self, master):
        self.master = master
        self.gui()
    def gui(self):
        #frame left
        self.frameLeft = Frame(self.master, bg="#FFCCCC", height=800, width=240)
        self.frameLeft.pack(side=LEFT, fill = Y)
        #logo
        image = "logo1.jpg"
        image_names = os.path.join(pathlib.Path(__file__).parent.absolute(), image)
        self.image = Image.open(image_names)
        self.image = self.image.resize((240, 200), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.image)
        self.logoLabel = Label(self.frameLeft, image=self.logo, bg="#FFCCCC")
        self.logoLabel.pack(side=TOP, fill = BOTH, padx=10 ,pady= 10)
        
        #Buttons
        self.ButtonFunc1 = Button(self.frameLeft, text="ADD NEW ITEM", bg="#FFCCCC", borderwidth=0, fg="black", font=("Nunito", 20), command= lambda: self.buttonFunc1())
        self.ButtonFunc1.pack(side=TOP, fill = BOTH, padx=10 ,pady= 30)

        self.ButtonFunc2 = Button(self.frameLeft, text="INVENTORY", bg="#FFCCCC", borderwidth=0, fg="black", font=("Nunito", 20), command= lambda: self.buttonFunc2())
        self.ButtonFunc2.pack(side=TOP, fill = BOTH, padx=10 ,pady= 30)

        self.ButtonFunc3 = Button(self.frameLeft, text="IMPORT ITEM", bg="#FFCCCC", borderwidth=0, fg="black", font=("Nunito", 20), command= lambda: self.buttonFunc3())
        self.ButtonFunc3.pack(side=TOP, fill = BOTH, padx=10 ,pady= 30)

        self.ButtonFunc4 = Button(self.frameLeft, text="EXPORT ITEM", bg="#FFCCCC", borderwidth=0, fg="black", font=("Nunito", 20), command= lambda: self.buttonFunc4())
        self.ButtonFunc4.pack(side=TOP, fill = BOTH, padx=10 ,pady= 30)

        #frame left end here
        self.activeFrame = Frame(self.master, bg="white", height=800, width=1040) 
        self.activeFrame.pack(side=TOP, fill = Y)
        image2 = "background.jpg"
        image2_names = os.path.join(pathlib.Path(__file__).parent.absolute(), image2)
        self.image2 = Image.open(image2_names)
        self.image2 = self.image2.resize((1018, 740), Image.ANTIALIAS)
        self.backGround = ImageTk.PhotoImage(self.image2)
        self.backGroundLabel = Label(self.activeFrame, image=self.backGround, bg="white")
        self.backGroundLabel.pack(side=TOP, fill = BOTH)
        

    
    # frame change function
    def buttonFunc1(self):
        self.activeFrame.destroy()
        self.activeFrame = Frame(self.master, bg="white", height=800, width=1040) 
        self.activeFrame.pack(side=TOP, fill = Y)
        fun1.fun1(self.activeFrame)

    def buttonFunc2(self):
        self.activeFrame.destroy()
        self.activeFrame = Frame(self.master, bg="white", height=800, width=1040) 
        self.activeFrame.pack(side=TOP, fill = Y)
        fun2.fun2(self.activeFrame)

    def buttonFunc3(self):
        self.activeFrame.destroy()
        self.activeFrame = Frame(self.master, bg="white", height=800, width=1040)
        self.activeFrame.pack(side=TOP, fill = Y)
        fun3.fun3(self.activeFrame)

    def buttonFunc4(self):
        self.activeFrame.destroy()
        self.activeFrame = Frame(self.master, bg="white", height=800, width=1040)
        self.activeFrame.pack(side=TOP, fill = Y)
        fun4.fun4(self.activeFrame)