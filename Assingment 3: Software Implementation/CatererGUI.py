from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class CatererGUI:   # create a GUI class for the caterer
    def __init__(self, data_layer):
        self.data_layer = data_layer  # Initialize data layer
        self.root = tk.Tk()  # Create a Tkinter root window
        self.root.geometry("450x450")  # Set window size
        self.root.title("Caterer Management System")  # Set window title

        # Labels and Entry fields
        self.id_label = tk.Label(self.root, text="ID:")   # create a label for ID
        self.id_label.grid(row=0, column=0, sticky=tk.W, pady=5)  # place the ID label in the grid
        self.id_entry = tk.Entry(self.root)  # create an entry field for ID
        self.id_entry.grid(row=0, column=1)  # place the ID entry field in the grid

        self.name_label = tk.Label(self.root, text="Name:")   # create a label for Name
        self.name_label.grid(row=1, column=0, sticky=tk.W, pady=5)  # place the Name label in the grid
        self.name_entry = tk.Entry(self.root)  # create an entry field for Name
        self.name_entry.grid(row=1, column=1)  # place the Name entry field in the grid

        self.address_label = tk.Label(self.root, text="Address:")   # create a label for Address
        self.address_label.grid(row=2, column=0, sticky=tk.W, pady=5)  # place the Address label in the grid
        self.address_entry = tk.Entry(self.root)  # create an entry field for Address
        self.address_entry.grid(row=2, column=1)  # place the Address entry field in the grid

        self.contact_label = tk.Label(self.root, text="Contact Details:")   # create a label for Contact Details
        self.contact_label.grid(row=3, column=0, sticky=tk.W, pady=5)  # place the Contact Details label in the grid
        self.contact_entry = tk.Entry(self.root)  # create an entry field for Contact Details
        self.contact_entry.grid(row=3, column=1)  # place the Contact Details entry field in the grid

        self.maxGuest_label = tk.Label(self.root, text="Max Guest:")   # create a label for Max Guest
        self.maxGuest_label.grid(row=4, column=0, sticky=tk.W, pady=5)  # place the Max Guest label in the grid
        self.maxGuest_entry = tk.Entry(self.root)  # create an entry field for Max Guest
        self.maxGuest_entry.grid(row=4, column=1)  # place the Max Guest entry field in the grid

        self.minGuest_label = tk.Label(self.root, text="Min Guest:")   # create a label for Min Guest
        self.minGuest_label.grid(row=5, column=0, sticky=tk.W, pady=5)  # place the Min Guest label in the grid
        self.minGuest_entry = tk.Entry(self.root)  # create an entry field for Min Guest
        self.minGuest_entry.grid(row=5, column=1)  # place the Min Guest entry field in the grid

        # Button to add caterer details
        self.add_button = tk.Button(self.root, text="Add Caterer", command=self.add_caterer)
        self.add_button.grid(row=6, column=0, pady=5)

        # Button to delete certain caterer details
        self.delete_button = tk.Button(self.root, text="Delete Caterer", command=self.delete_caterer)
        self.delete_button.grid(row=6, column=1, pady=5)

        # Button to modify certain caterer details
        self.modify_button = tk.Button(self.root, text="Modify Caterer", command=self.modify_caterer)
        self.modify_button.grid(row=7, column=0, pady=5)

        # Button to display caterer details in a table format
        self.display_button = tk.Button(self.root, text="Display Caterer Details", command=self.display_caterer_details)
        self.display_button.grid(row=7, column=1, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.maxGuest_entry.delete(0, tk.END)
        self.minGuest_entry.delete(0, tk.END)

    def add_caterer(self):  # define a function to add caterer details
        try:
            # Retrieve caterer details from entry fields
            caterer_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            max_guests = int(self.maxGuest_entry.get())
            min_guests = int(self.minGuest_entry.get())
            # create a Caterer object
            caterer = Caterer(caterer_id, name, address, contact_details, max_guests, min_guests)

            # Display the collected information
            print("Caterer added successfully:")
            print("ID:", caterer_id)
            print("Name:", name)
            print("Address:", address)
            print("Contact Details:", contact_details)
            print("Max Guests:", max_guests)
            print("Min Guests:", min_guests)

            # Retrieve existing caterers from data layer
            all_caterers = self.data_layer.read_all_caterers()

            # Check if ID already exists
            if caterer_id in all_caterers:
                # Display a message box informing the user that the caterer with the given ID already exists
                tk.messagebox.showinfo("ID Check", f"The ID '{caterer_id}' already exists for a caterer.")
            else:
                all_caterers[caterer_id] = caterer
                # Display a message box informing the user that the caterer details was added successfully
                tk.messagebox.showinfo("Caterer Added",f"The caterer with ID '{caterer_id}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_caterers_to_file(all_caterers)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)

    def delete_caterer(self):  # define a function to delete caterer details
        try:
            # Retrieve ID of Caterer to delete
            caterer_id = int(self.id_entry.get())
            # Retrieve existing caterers from data layer
            all_caterers = self.data_layer.read_all_caterers()

            # Check if ID already exists
            if caterer_id in all_caterers:
                # Delete the caterer
                del all_caterers[caterer_id]
                # Display a message box informing the user that the caterer details was deleted successfully
                tk.messagebox.showinfo("Caterer Deleted",f"The caterer with ID '{caterer_id}' has been deleted successfully.")
                # Write updated data to file
                self.data_layer.write_caterers_to_file(all_caterers)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the caterer with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The ID '{caterer_id}' does not exist for a caterer, do you want to add it?")

        except Exception as e:
            print("An error occurred:", e)

    def modify_caterer(self):  # define a function to modify caterer details
        try:
            # Retrieve modified caterer details from entry fields
            caterer_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            max_guests = int(self.maxGuest_entry.get())
            min_guests = int(self.minGuest_entry.get())
            # create an Caterer object
            caterer = Caterer(caterer_id, name, address, contact_details, max_guests, min_guests)

            # Retrieve existing caterers from data layer
            all_caterers = self.data_layer.read_all_caterers()

            # Check if ID already exists
            if caterer_id in all_caterers:
                all_caterers[caterer_id] = caterer
                # Display a message box informing the user that the caterer details was modified successfully
                tk.messagebox.showinfo("Caterer Modified", f"The caterer with ID '{caterer_id}' has been modified successfully.")
                # Write updated data to file
                self.data_layer.write_caterers_to_file(all_caterers)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the caterer with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The caterer with ID '{caterer_id}' does not exist")

        except Exception as e:
            print("An error occurred:", e)


    def display_caterer_details(self):  # define a function to display caterer details in a table format by calling the ListCatererForm
        # display the added caterer into the table created in the ListCatererForm class
        ListCatererForm(dt)


class ListCatererForm:
    """Class to represent a GUI form to display data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('1200x400')  # set window size
        self.root.title("Caterer Details")  # set window title

        # Create the table to display all caterer details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Address', 'Contact', 'Max Guests', 'Min Guests'), show='headings')
        # Set column heading for each attribute of the caterer
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Contact', text='Contact')
        self.table.heading('Max Guests', text='Max Guests')
        self.table.heading('Min Guests', text='Min Guests')
        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_caterers = self.data_layer.read_all_caterers()
        for caterer_id, caterer in all_caterers.items():
            # Insert caterer data into the table
            self.table.insert('', 'end', values=(caterer_id, caterer.get_name(), caterer.get_address(), caterer.get_contactDetails(), caterer.get_maxGuests(), caterer.get_minGuests()))

        self.root.mainloop()


class Caterer(Entity): # create a class for the caterer, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails, maxGuests, minGuests): # define a constructor method to initialize the attributes of the Caterer class
        super().__init__(id, name, address, contactDetails)  # call the attributes of the parent class
        self.__maxGuests = maxGuests
        self.__minGuests = minGuests

    def set_maxGuests(self, maxGuests):  # setter method for updating the maximum number of guests
        self.__maxGuests = maxGuests

    def set_minGuests(self, minGuests):  # setter method for updating the minimum number of guests
        self.__minGuests = minGuests

    def get_maxGuests(self):  # getter method for receiving the maximum number of guests
        return self.__maxGuests

    def get_minGuests(self):  # getter method for receiving the minimum number of guests
        return self.__minGuests

    def __str__(self):  # define a function to display information about the Caterer
        return super().__str__() + f", Caterer Maximum Guests: {self.__maxGuests}, Caterer Minimum Guests: {self.__minGuests}"


class DataLayer:
    """Class to handle read and write operations for caterer data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_caterers(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_caterers = pickle.load(file)
                    return all_caterers
        except Exception as e:
            print("An error occurred while reading venue data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_caterers_to_file(self, all_caterers):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the caterer data to the file
                pickle.dump(all_caterers, f)
                print("Caterer data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing caterer data to file:", e)


# Create an instance of the DataLayer class
filename = "caterer.pkl"
dt = DataLayer(filename)
# Create an instance of the CatererGUI class and pass the data_layer argument
venue_gui = CatererGUI(dt)
# Read all caterers from the data layer
all_caterers = dt.read_all_caterers()
# Create an instance of the ListCatererForm class to display caterer details
show_caterer = ListCatererForm(dt)