from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class GuestGUI:  # create a GUI class for the guest
    def __init__(self, data_layer):
        self.data_layer = data_layer  # Initialize data layer
        self.root = tk.Tk()  # Create a Tkinter root window
        self.root.geometry("450x450")  # Set window size
        self.root.title("Guest Management System")  # Set window title

        # Labels and Entry fields
        self.id_label = tk.Label(self.root, text="ID:")   # create a label for ID
        self.id_label.grid(row=0, column=0, sticky=tk.W, pady=5)  # place the ID label in the grid
        self.id_entry = tk.Entry(self.root)  # create an entry field for ID
        self.id_entry.grid(row=0, column=1)  # place the ID entry field in the grid

        self.name_label = tk.Label(self.root, text="Name:")   # create a label for Name
        self.name_label.grid(row=1, column=0, sticky=tk.W, pady=5)  # place the Name label in the grid
        self.name_entry = tk.Entry(self.root)  # create an entry field for Name
        self.name_entry.grid(row=1, column=1)   # place the Name entry field in the grid

        self.address_label = tk.Label(self.root, text="Address:")   # create a label for Address
        self.address_label.grid(row=2, column=0, sticky=tk.W, pady=5)  # place the Address label in the grid
        self.address_entry = tk.Entry(self.root)  # create an entry field for Address
        self.address_entry.grid(row=2, column=1)   # place the Address entry field in the grid

        self.contact_label = tk.Label(self.root, text="Contact Details:")   # create a label for Contact Detail
        self.contact_label.grid(row=3, column=0, sticky=tk.W, pady=5)  # place the Contact Detail label in the grid
        self.contact_entry = tk.Entry(self.root)  # create an entry field for Contact Detail
        self.contact_entry.grid(row=3, column=1)   # place the Contact Detail entry field in the grid

        self.status_label = tk.Label(self.root, text="Status:")   # create a label for Status
        self.status_label.grid(row=4, column=0, sticky=tk.W, pady=5)  # place the Status label in the grid
        self.status_entry = tk.Entry(self.root)  # create an entry field for Status
        self.status_entry.grid(row=4, column=1)   # place the Status entry field in the grid

        # Button to add guest details
        self.add_button = tk.Button(self.root, text="Add Guest", command=self.add_guest)
        self.add_button.grid(row=5, column=0, pady=5)

        # Button to delete certain guest details
        self.delete_button = tk.Button(self.root, text="Delete Guest", command=self.delete_guest)
        self.delete_button.grid(row=5, column=1, pady=5)

        # Button to modify certain guest details
        self.modify_button = tk.Button(self.root, text="Modify Guest", command=self.modify_guest)
        self.modify_button.grid(row=6, column=0, pady=5)

        # Button to display guest details in a table format
        self.display_button = tk.Button(self.root, text="Display Guest Details", command=self.display_guest_details)
        self.display_button.grid(row=6, column=1, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)

    def add_guest(self):  # define a function to add guest details
        try:
            # Retrieve guest details from entry fields
            guest_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            status = str(self.status_entry.get())
            # create a Guest object
            guest = Guest(guest_id, name, address, contact_details, status)

            # Display the collected information
            print("Guest added successfully:")
            print("ID:", guest_id)
            print("Name:", name)
            print("Address:", address)
            print("Contact Details:", contact_details)
            print("Budget:", status)

            # Retrieve existing guests from data layer
            all_guests = self.data_layer.read_all_guests()

            # Check if ID already exists
            if guest_id in all_guests:
                # Display a message box informing the user that the guest with the given ID already exists
                tk.messagebox.showinfo("ID Check", f"The ID '{guest_id}' already exists for a guest.")
            else:
                all_guests[guest_id] = guest
                # Display a message box informing the user that the guest details was added successfully
                tk.messagebox.showinfo("Guest Added",f"The guest with ID '{guest_id}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_guests_to_file(all_guests)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)

    def delete_guest(self):  # define a function to delete guest details
        try:
            # Retrieve guest ID to delete
            guest_id = int(self.id_entry.get())
            # Retrieve existing guests from data layer
            all_guests = self.data_layer.read_all_guests()
            # Check if the guest ID exists
            if guest_id in all_guests:
                # Delete the guest from the dictionary
                del all_guests[guest_id]
                # Display a message box informing the user that the guest details was deleted successfully
                tk.messagebox.showinfo("Guest Deleted", f"The guest with ID '{guest_id}' has been deleted successfully.")
                # Write updated data to file
                self.data_layer.write_guests_to_file(all_guests)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the guest with the given ID doesn't exist
                tk.messagebox.showinfo("Guest Not Found", f"The guest with ID '{guest_id}' does not exist.")

        except Exception as e:
            print("An error occurred:", e)

    def modify_guest(self):  # define a function to add guest details
        try:
            # Retrieve modified guest details from entry fields
            guest_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            status = str(self.status_entry.get())
            # create Guest object
            guest = Guest(guest_id, name, address, contact_details, status)

            # Retrieve existing guests from data layer
            all_guests = self.data_layer.read_all_guests()

            # Check if guest ID exists
            if guest_id in all_guests:
                # Update guest details
                all_guests[guest_id] = guest
                # Display a message box informing the user that the guest details was modified successfully
                tk.messagebox.showinfo("Guest Modified",f"The guest with ID '{guest_id}' has been modified successfully.")
                # Write updated data to file
                self.data_layer.write_guests_to_file(all_guests)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the guest with the given ID doesn't exist
                tk.messagebox.showinfo("Guest Not Found", f"The guest with ID '{guest_id}' does not exist.")

        except Exception as e:
            print("An error occurred:", e)


    def display_guest_details(self):  # define a function to display guest details in a table format by calling the ListGuestForm
        # display the added guest into the table that is created in the ListGuestForm class
        ListGuestForm(dt)


class ListGuestForm:
    """Class to represent a GUI form to display data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('1000x400')  # set window size
        self.root.title("Guest Details")  # set window title

        # Create the table to display all guest details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Address', 'Contact', 'Status'), show='headings')
        # Set column heading for each attribute of the guest
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Contact', text='Contact')
        self.table.heading('Status', text='Status')
        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_guests = self.data_layer.read_all_guests()
        for guest_id, guest in all_guests.items():
            # Insert guest data into the table
            self.table.insert('', 'end', values=(guest_id, guest.get_name(), guest.get_address(), guest.get_contactDetails(), guest.get_status()))

        self.root.mainloop()

class Guest(Entity): # create a class for the guest, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails, status): # define a constructor method to initialize the attributes of the Client class
        super().__init__(id, name, address, contactDetails) # call the attributes of the parent class
        self.__status = status

    def set_status(self, status): # setter method for updating the status
        self.__status = status

    def get_status(self): # getter method for receiving the status
        return self.__status

    def __str__(self): # define a function to display information about the Guest
        return super().__str__() + f", Guest Status: {self.__status}"

class DataLayer:
    """Class to handle read and write operations for guest data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_guests(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_guests = pickle.load(file)
                    return all_guests
        except Exception as e:
            print("An error occurred while reading guest data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_guests_to_file(self, all_guests):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the guest data to the file
                pickle.dump(all_guests, f)
                print("Guest data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing guest data to file:", e)


# Create an instance of the DataLayer class
filename = "guests.pkl"
dt = DataLayer(filename)
# Create an instance of the GuestGUI class and pass the data_layer argument
guest_gui = GuestGUI(dt)
# Read all guests from the data layer
all_guests = dt.read_all_guests()
# Create an instance of the ListGuestForm class to display guest details
show_guest = ListGuestForm(dt)