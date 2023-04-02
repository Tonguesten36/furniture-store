from tkinter import *
import tkinter.messagebox
import tkinter.ttk
import sqlite3

class fun3:
    def __init__(self, master):
        self.master = master
        self.header = Label(self.master, text="Export Furniture", bg="white", fg="black", font=("Times New Roman", 20))
        self.header.pack(side=TOP, fill = BOTH)
        self.cart = [] # Stores the ID of item's you want to purchase and how many of that item to buy (together as a dict,, add in the "item_index" key as well)
        self.item_index = 0 # The position of an item on the treeview, unique for each new item in the treeview
        self.fun3_gui()

    # GUI function
    def fun3_gui(self):
        self.activeFrame = Frame(self.master, bg="#009966", height=800, width=2000) 
        self.activeFrame.pack(side=TOP, fill = Y)
        self.mainFrame = Frame(self.activeFrame, bg="#FFCCCC", height=700, width=840, borderwidth=2, relief="groove")
        self.mainFrame.pack(side=TOP, fill = BOTH, padx=100, pady=40)

        # Labels
        self.EnterID = Label(self.mainFrame, text="Enter ID of the furniture: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.EnterID.place(x=50, y=50)
        self.Amount = Label(self.mainFrame, text="Enter amount of good: ", bg="#FFCCCC", fg="black", font=("Times New Roman", 20))
        self.Amount.place(x=50, y=100)
        
        # Entries
        self.ID = Entry(self.mainFrame, width=30, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.ID.place(x=350, y=50, height=40, width=200)
        self.Amount = Entry(self.mainFrame, width=30, font=("Times New Roman", 20), borderwidth=2, relief="groove")
        self.Amount.place(x=350, y=100, height=40, width=200)

        # Buttons
        self.search = Button(self.mainFrame, text="Add to cart", bg="#EE0000", fg="white", font=("Times New Roman", 20), command=self.add_furniture)
        self.search.place(x= 570, y=70, height=40, width=150)
        self.Export = Button(self.mainFrame, text="Confirm", bg="#EE0000", fg="white", font=("Times New Roman", 20), command=self.export_furniture)
        self.Export.place(x= 290, y=550, height=40, width=200)
        
        # Treeview is the cart
        self.tree = tkinter.ttk.Treeview(self.mainFrame, columns=('ID','Name', 'Export price', 'Quantity', 'Category'), show='headings')
        self.tree.column('ID', width=10)
        self.tree.column('Name', width=10)
        self.tree.column('Export price', width=10)
        self.tree.column('Quantity', width=10)
        self.tree.column('Category', width=10)
        self.tree.heading('ID', text='ID')        
        self.tree.heading('Name', text='Name')        
        self.tree.heading('Export price', text='Export price')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Category', text='Category')
        self.tree.place(x=22, y=160, height=370, width=700)
        
        # Scrollbar
        self.scrollbar = Scrollbar(self.mainFrame, orient="vertical", command=self.tree.yview)
        self.scrollbar.place(x=900, y=40, height=500)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
    # Search for an item in the inventory
    # if they exist then add the item with its quantity into the 'cart'
    def add_furniture(self, *args,**kwargs):
        self.furniture_ID = self.ID.get()
        self.furniture_amount = self.Amount.get()
        self.index = self.item_index

        if self.furniture_ID != "":
            if self.furniture_amount != "":
                # Initialize connection to the database
                db_connection = sqlite3.connect("store.db")
                db_cursor = db_connection.cursor()

                try:
                    # Search for the row with self.ID
                    search_item_query = f"SELECT * FROM inventory WHERE id={int(self.furniture_ID)};"
                    db_cursor.execute(search_item_query)                               
                except sqlite3.OperationalError: # This except block will occur if the entry field ID is not an integer
                    tkinter.messagebox.showerror("Failed", f"Cannot find furniture with the ID {self.furniture_ID}")
                else: # If nothing goes wrong then execut this code block
                    # Here, fetchone() is used to gather data of the row found afer execute the SQLite command in search_item_query
                    item_data = db_cursor.fetchone()
                    if item_data != None: # If the item is found in inventory, do the following...
                        # If the cart is empty then add the item into the list
                        if len(self.cart) == 0:                
                            # Create a new dictionary and increment the item_index by 1
                            new_item_dict = {}
                            new_item_dict.update({"id":item_data[0], "buy_quantity":int(self.furniture_amount), "export_price":item_data[4],"item_index":self.item_index})
                            self.item_index += 1

                            # Add the item into the treeview according to the item_index and the 'cart'
                            self.tree.insert('', self.item_index, values=(item_data[0], item_data[1], item_data[4], self.furniture_amount, item_data[3]))
                            self.cart.append(new_item_dict)
                            
                            # Let the user know that the item is added into the 'cart'
                            tkinter.messagebox.showinfo("Success", "Furniture added to cart successfully")
                        else:
                            # Iterate through the cart everytime the user click the button if the cart is not empty
                            for furniture in self.cart:
                                item_id = furniture.get("id")
                                # Get the item's current stock in the inventory...
                                get_item_stock_query = f"SELECT stock FROM inventory WHERE id={item_id};"
                                item_current_stock = db_cursor.execute(get_item_stock_query).fetchone()
                                # ...and the item's name as well
                                get_item_name_query = f"SELECT name FROM inventory WHERE id={item_id}"
                                item_name = db_cursor.execute(get_item_name_query).fetchone()
                                    
                                # Check if the user type in a new furniture ID
                                if item_id != int(self.furniture_ID):
                                    # Check if the user's request can be satisfied with the current stock of a specific item
                                    if self.furniture_amount <= item_current_stock[0]:
                                        # Create a new dictionary and increment the item_index by 1
                                        new_item_dict = {}
                                        new_item_dict.update({"id":item_data[0], "buy_quantity":int(self.furniture_amount), "export_price":item_data[4], "item_index":self.item_index})
                                        self.item_index += 1

                                        # Add the item into the treeview according to the item_index and the 'cart'
                                        self.tree.insert('', self.item_index, values=(item_data[0], item_data[1], item_data[4], self.furniture_amount, item_data[3]))
                                        self.cart.append(new_item_dict)
                                        
                                        # Let the user know that the item is added into the 'cart'
                                        tkinter.messagebox.showinfo("Success", "Furniture added to cart successfully")
                                        break
                                    else:
                                        tkinter.messagebox.showerror(f"Cannot buy item {item_name[0]}", "There is not enough of that item to buy")
                                        break
                                else: # And if they type in an ID from one of the items in the 'cart'...
                                    # Calculate the new amount of that item the user wanted to buy
                                    current_buy_quantity = furniture.get("buy_quantity")
                                    new_buy_quantity = current_buy_quantity + int(self.furniture_amount)

                                    # Then the item in the treeview should be updated with the new buy_quantity value,
                                    # assuming that the new_buy_quantity <= item's current stock in inventory     
                                    if new_buy_quantity <= item_current_stock[0]:                                  
                                        x = self.tree.get_children()
                                        self.tree.item(x, values=(item_data[0], item_data[1], item_data[4], new_buy_quantity, item_data[3]))
                                        furniture.update({"buy_quantity":new_buy_quantity})
                                        break
                                    else:
                                        tkinter.messagebox.showerror(f"Cannot buy item {item_name[0]}", "There is not enough of that item to buy")
                                        break
                    else: # if the item is not in inventory, tell the user that the item does not exist in the table 
                        tkinter.messagebox.showerror("Failed", f"Cannot find furniture with the ID {int(self.furniture_ID)}")
                        self.ID.delete(0, END)
                finally: 
                    # Close the connection regardless of whatever happened
                    db_cursor.close()
                    self.ID.delete(0, END)
                    self.Amount.delete(0, END)
            else:
                tkinter.messagebox.showerror("Error", "Missing quantity, must be a non-zero value")
        else:
            tkinter.messagebox.showerror("Error", "Please input furniture ID")
    
    # Manage the export and import of the furniture
    def export_furniture(self, *args,**kwargs):
        # Establish connection to database
        db_connection = sqlite3.connect("store.db")
        db_cursor = db_connection.cursor()
        
        transaction_fee = 0        

        if len(self.cart) != 0:
            # Look through every item in the cart (if it is not empty)
            for item in self.cart:
                # Get the current stock quantity of the item
                item_id = item.get("id")
                get_item_stock_query = f"SELECT stock FROM inventory WHERE id={item_id};"

                # Execute the SQL command and fetch the data from the cursor
                current_item_stock = db_cursor.execute(get_item_stock_query).fetchone()

                # How many of that item does the user want to buy ?
                item_buy_quantity = int(item.get("buy_quantity")) 
                # What is the export price of that item individually?
                item_export_price = int(item.get("export_price")) 

                # Calculate the transaction fee until the for loop ends
                transaction_fee += item_buy_quantity * item_export_price

                # Update the item's stock and commit the change to the table
                update_quantity_query = f"UPDATE inventory SET stock={current_item_stock[0] - item_buy_quantity} WHERE id={item_id};"
                db_cursor.execute(update_quantity_query)
                db_connection.commit()
            
            # Close the connection to database
            db_cursor.close()
            
            # Let the user know how much the transaction costs
            tkinter.messagebox.showinfo("Success", f"Total cost of the transaction is: {transaction_fee}")
            # Clean up the cart, treeview; and reset item_index to 0
            self.cart.clear()
            for item in self.tree.get_children():
                self.tree.delete(item)
                self.item_index = 0
        else:
            tkinter.messagebox.showerror("Failed", "The cart is empty")
            db_cursor.close()            
