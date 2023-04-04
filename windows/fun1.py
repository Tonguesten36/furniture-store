from tkinter import *
from tkcalendar import DateEntry
import tkinter.messagebox
import sqlite3

# Insert an item into the database
class fun1:
    def __init__(self, master):
        self.master = master
        self.header = Label(self.master, text="ADD NEW ITEM", bg="#009966", fg="#FFFF33", font=("Times New Roman", 20))
        self.header.pack(side=TOP, fill = BOTH)
        self.fun1_gui()
    
    # GUI function
    def fun1_gui(self):
        self.activeFrame = Frame(self.master, bg="#009966", height=800, width=2000) 
        self.activeFrame.pack(side=TOP, fill = BOTH)
        self.mainFrame = Frame(self.activeFrame, bg="#FFCCCC", height=700, width=840, borderwidth=2, relief="groove")
        self.mainFrame.pack(side=TOP, padx=100, pady=40, fill = BOTH)
        
        # Labels for the main frame
        self.label1 = Label(self.mainFrame, text="Furniture ID: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.label1.place(x=50, y=50)
        self.label2 = Label(self.mainFrame, text="Furniture Import Date: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.label2.place(x=50, y=120)
        self.label3 = Label(self.mainFrame, text="Furniture Name: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.label3.place(x=50, y=190)
        self.label4 = Label(self.mainFrame, text="Furniture Import Price: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.label4.place(x=50, y=260)
        self.label5 = Label(self.mainFrame, text="Furniture Export Price: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.label5.place(x=50, y=330)
        self.label6 = Label(self.mainFrame, text="Furniture Quantity: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.label6.place(x=50, y=400)
        self.label7 = Label(self.mainFrame, text="Furniture Category: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.label7.place(x=50, y=470)
        
        # Entry boxes for the main frame
        self.entry1 = Entry(self.mainFrame, width=26, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry1.place(x=320, y=50)
        self.entry2 = DateEntry(self.mainFrame, date_pattern= 'yyyy-MM-dd', width=25, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry2.place(x=320, y=120)
        self.entry3 = Entry(self.mainFrame, width=26, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry3.place(x=320, y=190)
        self.entry4 = Entry(self.mainFrame, width=26, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry4.place(x=320, y=260)
        self.entry5 = Entry(self.mainFrame, width=26, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry5.place(x=320, y=330)
        self.entry6 = Entry(self.mainFrame, width=26, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry6.place(x=320, y=400)
        self.entry7 = Entry(self.mainFrame, width=26, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.entry7.place(x=320, y=470)

        # Buttons import furniture
        self.addButton = Button(self.mainFrame, text="Import to Inventory", bg="#EE0000", fg="white", font=("Times New Roman", 20), borderwidth=2, relief="groove", command= self.get_infos)
        self.addButton.place(x=250, y=535)
    
    # Get info
    def get_infos(self, *args, **kwargs):
        # Get these data from the entries
        self.furniture_id = self.entry1.get()
        self.furniture_import_date = self.entry2.get()
        self.furniture_name = self.entry3.get()
        self.furniture_import_price = self.entry4.get()
        self.furniture_export_price = self.entry5.get()
        self.furniture_quantity = self.entry6.get()
        self.furniture_category = self.entry7.get()

        if self.furniture_id == "" or self.furniture_name == "" or self.furniture_category == "" or self.furniture_import_price == "" or self.furniture_export_price == "" or self.furniture_quantity == "" or self.furniture_import_date == "":
            tkinter.messagebox.showerror("Error", "Please fill all the fields!")
        else:
            # Initialize connection to the database
            db_connection = sqlite3.connect("store.db")
            db_cursor = db_connection.cursor()

            # Insert the new item into the table inventory
            insert_item_query = "INSERT INTO inventory (id, name, buy_date, category, buy_price, sell_price, stock) VALUES (?,?,?,?,?,?,?);"
            try:
                db_cursor.execute(insert_item_query, (self.furniture_id, self.furniture_name, self.furniture_import_date, self.furniture_category, self.furniture_import_price, self.furniture_export_price, self.furniture_quantity))
            
            except sqlite3.IntegrityError:
                tkinter.messagebox.showerror("Error", "Furniture ID already exists!")
            else:
            #messagebox to show success
                tkinter.messagebox.showinfo("Success", f"Furniture imported successfully!\nTotal value: {self.furniture_quantity} * {self.furniture_import_price} = {int(self.furniture_quantity) * int(self.furniture_import_price)}")
                db_connection.commit()
            finally:   
                db_cursor.close()
                self.entry1.delete(0, END)
                self.entry2.delete(0, END)
                self.entry3.delete(0, END)
                self.entry4.delete(0, END)
                self.entry5.delete(0, END)
                self.entry6.delete(0, END)
                self.entry7.delete(0, END)