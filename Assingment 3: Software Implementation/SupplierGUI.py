from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class SupplierGUI:  # create a GUI class for the supplier
    def __init__(self, data_layer):
        self.data_layer = data_layer  # Initialize data layer
        self.root = tk.Tk()  # Create a Tkinter root window
        self.root.geometry("400x400")  # Set window size
        self.root.title("Supplier Management System")  # Set window title

        # Labels and Entry fields
        self.id_label = tk.Label(self.root, text="ID:")  # create a label for ID
        self.id_label.grid(row=0, column=0,  sticky=tk.W, pady=5)  # place the ID label in the grid
        self.id_entry = tk.Entry(self.root)  # create an entry field for ID
        self.id_entry.grid(row=0, column=1)  # place the ID entry field in the grid

        self.name_label = tk.Label(self.root, text="Name:")  # create a label for Name
        self.name_label.grid(row=1, column=0, sticky=tk.W, pady=5)  # place the Name label in the grid
        self.name_entry = tk.Entry(self.root)  # create an entry field for Name
        self.name_entry.grid(row=1, column=1)  # place the Name entry field in the grid

        self.address_label = tk.Label(self.root, text="Address:")  # create a label for Address
        self.address_label.grid(row=2, column=0,  sticky=tk.W, pady=5)  # place the Address label in the grid
        self.address_entry = tk.Entry(self.root)  # create an entry field for Address
        self.address_entry.grid(row=2, column=1)  # place the Address entry field in the grid

        self.contact_label = tk.Label(self.root, text="Contact Details:")  # create a label for Contact Details
        self.contact_label.grid(row=3, column=0,  sticky=tk.W, pady=5)  # place the Contact Details label in the grid
        self.contact_entry = tk.Entry(self.root)  # create an entry field for Contact Details
        self.contact_entry.grid(row=3, column=1)  # place the Contact Details entry field in the grid

        # Button to add supplier details
        self.add_button = tk.Button(self.root, text="Add Supplier", command=self.add_supplier)
        self.add_button.grid(row=4, column=0, pady=5)

        # Button to delete certain supplier details
        self.delete_button = tk.Button(self.root, text="Delete Supplier", command=self.delete_supplier)
        self.delete_button.grid(row=4, column=1, pady=5)

        # Button to modify certain supplier details
        self.modify_button = tk.Button(self.root, text="Modify Supplier", command=self.modify_supplier)
        self.modify_button.grid(row=5, column=0, pady=5)

        # Button to display supplier details in a table format
        self.display_button = tk.Button(self.root, text="Display Supplier Details", command=self.display_supplier_details)
        self.display_button.grid(row=5, column=1, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)

    def add_supplier(self):  # define a function to add supplier details
        try:
            # Retrieve supplier details from entry fields
            supplier_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            # create a Supplier object
            supplier = Supplier(supplier_id, name, address, contact_details)

            # Display the collected information
            print("Supplier added successfully:")
            print("ID:", supplier_id)
            print("Name:", name)
            print("Address:", address)
            print("Contact Details:", contact_details)

            # Retrieve existing suppliers from data layer
            all_suppliers = self.data_layer.read_all_supplier()

            # Check if ID already exists
            if supplier_id in all_suppliers:
                # Display a message box informing the user that the supplier with the given ID already exists
                tk.messagebox.showinfo("ID Check", f"The ID '{supplier_id}' already exists for a supplier.")
            else:
                all_suppliers[supplier_id] = supplier
                # Display a message box informing the user that the supplier details was added successfully
                tk.messagebox.showinfo("Supplier Added",f"The supplier with ID '{supplier_id}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_supplier_to_file(all_suppliers)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)

    def delete_supplier(self):  # define a function to delete supplier details
        try:
            # Retrieve ID of Supplier to delete
            supplier_id = int(self.id_entry.get())
            # Retrieve existing suppliers from data layer
            all_suppliers = self.data_layer.read_all_supplier()

            # Check if ID already exists
            if supplier_id in all_suppliers:
                # Delete the supplier
                del all_suppliers[supplier_id]
                # Display a message box informing the user that the supplier details was deleted successfully
                tk.messagebox.showinfo("Supplier Deleted",f"The supplier with ID '{supplier_id}' has been deleted successfully")
                # Write updated data to file
                self.data_layer.write_supplier_to_file(all_suppliers)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the supplier with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The supplier with ID '{supplier_id}' does not exist")

        except Exception as e:
            print("An error occurred:", e)

    def modify_supplier(self):  # define a function to modify supplier details
        try:
            # Retrieve modified supplier details from entry fields
            supplier_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            # create a Supplier object
            supplier = Supplier(supplier_id, name, address, contact_details)

            # Retrieve existing suppliers from data layer
            all_suppliers = self.data_layer.read_all_supplier()

            # Check if ID already exists
            if supplier_id in all_suppliers:
                all_suppliers[supplier_id] = supplier
                # Display a message box informing the user that the supplier details was modified successfully
                tk.messagebox.showinfo("Supplier Modified",f"The venue with ID '{supplier_id}' has been modified successfully.")
                # Write updated data to file
                self.data_layer.write_supplier_to_file(all_suppliers)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the supplier with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The ID '{supplier_id}' does not exist for a supplier, do you want to add it?.")

        except Exception as e:
            print("An error occurred:", e)

    def display_supplier_details(self):  # define a function to display supplier details in a table format by calling the ListSupplierForm
        # display the added supplier into the table created in the ListSupplierForm class
        ListSupplierForm(dt)


class ListSupplierForm:
    """Class to represent a GUI form to display data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('800x300')  # set window size
        self.root.title("Supplier Details")  # set window title

        # Create the table to display all supplier details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Address', 'Contact Details'), show='headings')
        # Set column heading for each attribute of the supplier
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Contact Details', text='Contact Details')
        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_suppliers = self.data_layer.read_all_supplier()
        for supplier_id, supplier in all_suppliers.items():
            # Insert supplier data into the table
            self.table.insert('', 'end', values=(supplier_id, supplier.get_name(), supplier.get_address(), supplier.get_contactDetails()))

        self.root.mainloop()


class Supplier(Entity): # create a class for the supplier, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails): # define a constructor method to initialize the attributes of the Supplier class
        super().__init__(id, name, address, contactDetails) # call the attributes of the parent class

    def __str__(self): # define a function to display information about the Supplier
        return super().__str__()

class DataLayer:
    """Class to handle read and write operations for supplier data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_supplier(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_suppliers = pickle.load(file)
                    return all_suppliers
        except Exception as e:
            print("An error occurred while reading supplier data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_supplier_to_file(self, all_suppliers):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the supplier data to the file
                pickle.dump(all_suppliers, f)
                print("Supplier data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing supplier data to file:", e)


# Create an instance of the DataLayer class
filename = "supplier.pkl"
dt = DataLayer(filename)
# Create an instance of the SupplierGUI class and pass the data_layer argument
supplier_gui = SupplierGUI(dt)
# Read all suppliers from the data layer
all_suppliers = dt.read_all_supplier()
# Create an instance of the ListSupplierForm class to display supplier details
show_supplier = ListSupplierForm(dt)