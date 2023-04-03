from tkinter import *
from tkinter.ttk import Treeview

import tkinter.messagebox
import sqlite3

# List all item in the database
class fun2:
    def __init__(self, master):
        self.master = master
        self.header = Label(self.master, text="INVENTORY", bg="#009966", fg="#FFFF33", font=("Times New Roman", 20))
        self.header.pack(side=TOP, fill = BOTH)
        self.fun2_gui()
    
    # GUI function
    def fun2_gui(self):
        self.activeFrame = Frame(self.master, bg="#009966", height=800, width=2000) 
        self.activeFrame.pack(side=TOP, fill = Y)

        # Treeview take information from database
        self.tree = Treeview(self.activeFrame, columns=('ID', 'Name', 'Import date', 'Category', 'Import price', 'Export price', 'Quantity'), show='headings')
        self.tree.column('ID', width=10)
        self.tree.column('Name', width=10)
        self.tree.column('Import date', width=10)
        self.tree.column('Category', width=10)
        self.tree.column('Import price', width=10)
        self.tree.column('Export price', width=10)
        self.tree.column('Quantity', width=10)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Import date', text='Import date')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Import price', text='Import price')
        self.tree.heading('Export price', text='Export price')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.place(x=40, y=40, height=500, width=860)
        
        # Scrollbar
        self.scrollbar = Scrollbar(self.activeFrame, orient="vertical", command=self.tree.yview)
        self.scrollbar.place(x=900, y=40, height=500)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Button for confirm searching a specific item
        self.btn = Button(self.activeFrame, text="Search",bg="#EE0000", fg="white", font=("Times New Roman", 20), command=self.search_ID)
        self.btn.place(x=560, y=580, height=30, width=200)
        
        # Entry for searching a specific item
        self.entry = Entry(self.activeFrame, width=70, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry.place(x=290, y=580, height=30, width=200)
        
        # Label
        self.label = Label(self.activeFrame, text="Input furniture ID:",bg="#009966", fg="#FFFF33", font=("Times New Roman", 20))
        self.label.place(x=80, y=580, height=30, width=200)
        
        # List all item in the database
        self.list_item()
        
    #Search for a specific item
    def search_ID(self, *args,**kwargs):
        self.furniture_ID= self.entry.get()
        if self.furniture_ID == "":
            tkinter.messagebox.showerror("Error", "Please input furniture ID")
        else:
            # Initialize connection to the database
            db_connection = sqlite3.connect("store.db")
            db_cursor = db_connection.cursor()

            try:
                # Search for the row with self.ID
                search_item_query = f"SELECT * FROM inventory WHERE id={self.furniture_ID};"
                db_cursor.execute(search_item_query)

                # Display search result
                # Here, fetchone() is used to gather data of the row found afer execute the SQLite command in search_item_query
                item_data = db_cursor.fetchone()
                if item_data == None:
                    # if the item is not in inventory
                    # tell the user that the item does not exist in the table
                    tkinter.messagebox.showerror("Failed", f"Cannot find furniture with the ID {self.furniture_ID}")
                else:
                    # if the item is found in inventory
                    # display each column in the row
                    tkinter.messagebox.showinfo("Success",
                        f"ID: {item_data[0]}\n"\
                        f"Name: {item_data[1]}\n"\
                        f"Import Date: {item_data[2]}\n"\
                        f"Category: {item_data[3]}\n"\
                        f"Import Price: {item_data[4]}\n"\
                        f"Export Price: {item_data[5]}\n"\
                        f"Quantity: {item_data[6]}")
            except sqlite3.OperationalError: # This except block will occur if the entry field is not an integer
                tkinter.messagebox.showerror("Failed", f"Cannot find furniture with the ID {self.furniture_ID}")
            finally:
                # Close the connection
                db_cursor.close()
                self.entry.delete(0, END)

    # List all items inside the database
    def list_item(self):
        # Initialize connection to the database
        db_connection = sqlite3.connect("store.db")
        db_cursor = db_connection.cursor()

        # Display the items in the treeview
        list_all_query = "SELECT * FROM inventory"
        index = 0
        for row in db_cursor.execute(list_all_query):
            self.tree.insert('', index, values=row)                
            index += 1

        # Close the connection
        db_cursor.close()
