from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
import tkinter.messagebox
import sqlite3
import os, pathlib


class dashboard:
    def __init__(self, master):
        self.master = master
        self.header = Label(self.master, text="DASHBOARD", bg="#009966", fg="#FFFF33", font=("Times New Roman", 20))
        self.header.pack(side=TOP, fill = BOTH)
        self.db_gui()
    
    # GUI function
    def db_gui(self):
        self.activeFrame = Frame(self.master, bg="#009966", height=800, width=2000) 
        self.activeFrame.pack(side=TOP, fill = BOTH)
        
        # total products
        self.total = Image.open("./images/total.jpg")
        self.total_Resize = self.total.resize((200, 200), Image.ANTIALIAS)
        self.total_Resize = ImageTk.PhotoImage(self.total_Resize)
        self.totalLabel = tk.Button(self.activeFrame, image=self.total_Resize, command=self.total_products)
        self.totalLabel.place(x=35, y=60)
        
        # sold products
        self.sold = Image.open("./images/sold.jpg")
        self.sold_Resize = self.sold.resize((200, 200), Image.ANTIALIAS)
        self.sold_Resize = ImageTk.PhotoImage(self.sold_Resize)
        self.soldLabel = tk.Button(self.activeFrame, image=self.sold_Resize, command=self.sold_products)
        self.soldLabel.place(x=285, y=60)

        # total revenue
        self.revenue = Image.open("./images/revenue.jpg")
        self.revenue_Resize = self.revenue.resize((200, 200), Image.ANTIALIAS)
        self.revenue_Resize = ImageTk.PhotoImage(self.revenue_Resize)
        self.revenueLabel = tk.Button(self.activeFrame, image=self.revenue_Resize, command=self.total_revenue)
        self.revenueLabel.place(x=535, y=60)

        # total categories
        self.category = Image.open("./images/category.jpg")
        self.category_Resize = self.category.resize((200, 200), Image.ANTIALIAS)
        self.category_Resize = ImageTk.PhotoImage(self.category_Resize)
        self.categoryLabel = tk.Button(self.activeFrame, image=self.category_Resize, command=self.total_categories)
        self.categoryLabel.place(x=785, y=60)

    # TODO: show total products
    def total_products(self):
        # Establish the connection to the database
        # and initialize a cursor object
        db_connection = sqlite3.connect("store.db")
        db_cursor = db_connection.cursor()

        # Get the quantity of each item name in the inventory table
        select_item_quantity_query = "SELECT stock from inventory"
        db_cursor.execute(select_item_quantity_query)
        
        # the cursor object return an iterable of tuples with fetchall()
        # and store them in all_item_quantity 
        # with quantity of each item name at the first index of each tuple
        all_item_quantity = db_cursor.fetchall()
        
        # Calculate the total products
        # i[0] is the quantity of an item
        products = 0
        for i in all_item_quantity:
            products += i[0]

        tkinter.messagebox.showinfo("Total Products", f"Total Products in the inventory is: {products}")
    
    # TODO: show total revenue
    def total_revenue(self):    
        tkinter.messagebox.showinfo("Total Revenue")

    # Show total distinct categories
    def total_categories(self):
        # Establish the connection to the database
        # and initialize a cursor object
        db_connection = sqlite3.connect("store.db")
        db_cursor = db_connection.cursor()

        # First, you get a list of unique category
        get_distinct_category_query = "SELECT DISTINCT category FROM inventory"
        db_cursor.execute(get_distinct_category_query)

        # Like above, the cursor return an iterable of tuples
        distinct_categories = db_cursor.fetchall()

        # Since the total categories in the inventory only count distinct categories
        # We would only need the size of distinct_categories for total_categories
        total_categories = len(distinct_categories)

        tkinter.messagebox.showinfo("Total Categories", f"Total categories in inventory is: {total_categories}")
    
    # TODO: show sold products
    def sold_products(self):
        tkinter.messagebox.showinfo("Sold Products")
    

        
        
       


        
