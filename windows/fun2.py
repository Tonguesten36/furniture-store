from tkinter import *
from tkinter.ttk import Treeview
import tkinter.messagebox
class fun2:
    def __init__(self, master):
        self.master = master
        self.header = Label(self.master, text="Inventory", bg="white", fg="black", font=("Times New Roman", 20))
        self.header.pack(side=TOP, fill = BOTH)
        self.fun2_gui()
    def fun2_gui(self):
        self.activeFrame = Frame(self.master, bg="", height=800, width=2000) 
        self.activeFrame.pack(side=TOP, fill = Y)
        # Treeview take information from database
        self.tree = Treeview(self.activeFrame, columns=('ID', 'Import date','Name', 'Import price', 'Export price', 'Quantity', 'Category'), show='headings')
        self.tree.column('ID', width=10)
        self.tree.column('Import date', width=10)
        self.tree.column('Name', width=10)
        self.tree.column('Import price', width=10)
        self.tree.column('Export price', width=10)
        self.tree.column('Quantity', width=10)
        self.tree.column('Category', width=10)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Import date', text='Import date')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Import price', text='Import price')
        self.tree.heading('Export price', text='Export price')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Category', text='Category')
        self.tree.place(x=40, y=40, height=500, width=860)
        # Scrollbar
        self.scrollbar = Scrollbar(self.activeFrame, orient="vertical", command=self.tree.yview)
        self.scrollbar.place(x=900, y=40, height=500)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        # Button
        self.btn = Button(self.activeFrame, text="Search",bg="white", fg="black", font=("Times New Roman", 20), command=self.search_ID)
        self.btn.place(x=560, y=580, height=30, width=200)
        # Entry
        self.entry = Entry(self.activeFrame, width=70, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry.place(x=290, y=580, height=30, width=200)
        # Label
        self.label = Label(self.activeFrame, text="Input furniture ID:",bg="white", fg="black", font=("Times New Roman", 20))
        self.label.place(x=80, y=580, height=30, width=200)
        
    # Search function
    def search_ID(self, *args,**kwargs):
        self.ID= self.entry.get()
        if self.ID == "":
            tkinter.messagebox.showerror("Error", "Please input furniture ID")
        else:
            # add furniture to database
            # messagebox to show success
            tkinter.messagebox.showinfo("Success", "Search furniture successfully")
            self.entry.delete(0, END)

    



    





    

  

        

    
