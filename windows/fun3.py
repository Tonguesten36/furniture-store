from tkinter import *
import tkinter.messagebox
class fun3:
    def __init__(self, master):
        self.master = master
        self.header = Label(self.master, text="Export Furniture", bg="white", fg="black", font=("Times New Roman", 20))
        self.header.pack(side=TOP, fill = BOTH)
        self.fun3_gui()
    def fun3_gui(self):
        self.activeFrame = Frame(self.master, bg="", height=800, width=2000) 
        self.activeFrame.pack(side=TOP, fill = Y)
        self.mainFrame = Frame(self.activeFrame, bg="white", height=700, width=840, borderwidth=2, relief="groove")
        self.mainFrame.pack(side=TOP, fill = BOTH, padx=100, pady=40)

        # Label
        self.EnterID = Label(self.mainFrame, text="Enter ID of the furniture: ", bg="white", fg="black", font=("Times New Roman", 20))
        self.EnterID.place(x=50, y=50)
        self.Amount = Label(self.mainFrame, text="Give Amount: ", bg="white", fg="black", font=("Times New Roman", 20))
        self.Amount.place(x=50, y=400)
        # Entry
        self.ID = Entry(self.mainFrame, width=30, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.ID.place(x=350, y=50, height=40, width=200)
        self.Amount = Entry(self.mainFrame, width=30, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.Amount.place(x=250, y=400, height=40, width=200)

        # Button
        self.search = Button(self.mainFrame, text="Search", bg="white", fg="black", font=("Times New Roman", 20), command=self.search_furniture)
        self.search.place(x= 600, y=50, height=40, width=100)

        self.Export = Button(self.mainFrame, text="Calculate Change ", bg="white", fg="black", font=("Times New Roman", 20))
        self.Export.place(x= 500, y=400, height=40, width=230)
        # Search function
    def search_furniture(self, *args,**kwargs):
        self.search_furniture = self.ID.get()
        
        if self.search_furniture == "":
            tkinter.messagebox.showerror("Error", "Please input furniture ID")
        else:
            # add furniture to database
            # messagebox to show success
            tkinter.messagebox.showinfo("Success", "Search furniture successfully")
            self.ID.delete(0, END)
    #def export_furniture(self, *args,**kwargs):
    #trừ số lượng trong database và tính tiền bán
        

        
