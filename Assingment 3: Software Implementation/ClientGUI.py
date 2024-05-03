from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class ClientGUI: # create a GUI class for the client
    def __init__(self, data_layer):
        self.data_layer = data_layer # Initialize data layer
        self.root = tk.Tk() # Create a Tkinter root window
        self.root.geometry("500x500") # Set window size
        self.root.title("Client Management System") # Set window title

        # Labels and Entry fields
        self.id_label = tk.Label(self.root, text="ID:")  # create a label for ID
        self.id_label.grid(row=0, column=0, sticky=tk.W, pady=5)  # place the ID label in the grid
        self.id_entry = tk.Entry(self.root)  # create an entry field for ID
        self.id_entry.grid(row=0, column=1)  # place the ID entry field in the grid

        self.name_label = tk.Label(self.root, text="Name:")  # create a label for Name
        self.name_label.grid(row=1, column=0, sticky=tk.W, pady=5)  # place the Name label in the grid
        self.name_entry = tk.Entry(self.root)  # create an entry field for Name
        self.name_entry.grid(row=1, column=1)  # place the Name entry field in the grid

        self.address_label = tk.Label(self.root, text="Address:")  # create a label for Address
        self.address_label.grid(row=2, column=0, sticky=tk.W, pady=5)  # place the Address label in the grid
        self.address_entry = tk.Entry(self.root)  # create an entry field for Address
        self.address_entry.grid(row=2, column=1)  # place the Address entry field in the grid

        self.contact_label = tk.Label(self.root, text="Contact Details:")  # create a label for Contact Details
        self.contact_label.grid(row=3, column=0, sticky=tk.W, pady=5)  # place the Contact Details label in the grid
        self.contact_entry = tk.Entry(self.root)  # create an entry field for Contact Details
        self.contact_entry.grid(row=3, column=1)  # place the Contact Details entry field in the grid

        self.budget_label = tk.Label(self.root, text="Budget:")  # create a label for Budget
        self.budget_label.grid(row=4, column=0, sticky=tk.W, pady=10)  # place the Budget label in the grid
        self.budget_entry = tk.Entry(self.root)  # create an entry field for Budget
        self.budget_entry.grid(row=4, column=1)  # place the Budget entry field in the grid

        # Button to add client details
        self.add_button = tk.Button(self.root, text="Add Client", command=self.add_client)
        self.add_button.grid(row=5, column=0, pady=5)

        # Button to delete certain client details
        self.delete_button = tk.Button(self.root, text="Delete Client", command=self.delete_client)
        self.delete_button.grid(row=5, column=1, pady=5)

        # Button to modify certain client details
        self.modify_button = tk.Button(self.root, text="Modify Client", command=self.modify_client)
        self.modify_button.grid(row=6, column=0, pady=5)

        # Button to display client details in a table format
        self.display_button = tk.Button(self.root, text="Display Client Details", command=self.display_client_details)
        self.display_button.grid(row=6, column=1, pady=5)

        # Button to display events associated with a client
        self.add_events_button = tk.Button(self.root, text="Add Events", command=self.add_client_events)
        self.add_events_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)

    def add_client(self):  # define a function to add a client
        try:
            # Retrieve client details from entry fields
            client_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            budget = float(self.budget_entry.get())
            # create a Client object
            client = Client(client_id, name, address, contact_details, budget)

            # Display the collected information
            print("Client added successfully:")
            print("ID:", client_id)
            print("Name:", name)
            print("Address:", address)
            print("Contact Details:", contact_details)
            print("Budget:", budget)

            # Retrieve existing clients from data layer
            all_clients = self.data_layer.read_all_clients()

            # Check if ID already exists
            if client_id in all_clients:
                # Display a message box informing the user that the client with the given ID already exists
                tk.messagebox.showinfo("ID Check", f"The ID '{client_id}' already exists for a client.")
            else:
                all_clients[client_id] = client
                # Display a message box informing the user that the client details was added successfully
                tk.messagebox.showinfo("Client Added",f"The client with ID '{client_id}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_clients_to_file(all_clients)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)

    def delete_client(self):  # define a function to delete client details
        try:
            # Retrieve client ID to delete
            client_id = int(self.id_entry.get())
            # Retrieve existing clients from data layer
            all_clients = self.data_layer.read_all_clients()
            # Check if the client ID exists
            if client_id in all_clients:
                # Delete the client from the dictionary
                del all_clients[client_id]
                # Display a message box informing the user that the client details was deleted successfully
                tk.messagebox.showinfo("Client Deleted", f"The client with ID '{client_id}' has been deleted successfully.")
                # Write updated data to file
                self.data_layer.write_clients_to_file(all_clients)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the client with the given ID doesn't exist
                tk.messagebox.showinfo("Client Not Found", f"The client with ID '{client_id}' does not exist.")

        except Exception as e:
            print("An error occurred:", e)

    def modify_client(self):  # define a function to modify client details
        try:
            # Retrieve modified client details from entry fields
            client_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            budget = str(self.budget_entry.get())
            # create a client object
            client = Client(client_id, name, address, contact_details, budget)

            # Retrieve existing clients from data layer
            all_clients = self.data_layer.read_all_clients()

            # Check if client ID exists
            if client_id in all_clients:
                # Update client details for a specified id
                all_clients[client_id] = client
                # Display a message box informing the user that the client details was modified successfully
                tk.messagebox.showinfo("Client Modified",f"The client with ID '{client_id}' has been modified successfully.")
                # Write updated data to file
                self.data_layer.write_clients_to_file(all_clients)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the client with the given ID doesn't exist
                tk.messagebox.showinfo("Client Not Found", f"The client with ID '{client_id}' does not exist.")

        except Exception as e:
            print("An error occurred:", e)


    def add_client_events(self):  # define a function to add events to the clients
        try:
            # Retrieve client ID from entry field
            client_id = int(self.id_entry.get())
            # Retrieve existing clients from data layer
            all_clients = self.data_layer.read_all_clients()
            # Check if client ID exists
            if client_id in all_clients:
                client = all_clients[client_id]
                # create composition - add an event that will be organized by a certain client
                client.add_event(2, "Birthday", "Princess", "May 5", "2:00", "4 hours", "Elm St", None, None, "Party Decor Inc.", "Magic Moments", "Event Essentials", None)
                # Write updated data to file
                self.data_layer.write_clients_to_file(all_clients)
                # Display a message box informing the user that the event was added to the client successfully
                tk.messagebox.showinfo("Event Added", f"The event organized by the client with ID: '{client_id}' has been added succesfully")

            else:
                # Display a message box informing the user that the client with the given ID doesn't exist
                tk.messagebox.showinfo("Client Not Found", f"The client with ID '{client_id}' does not exist.")

        except Exception as e:
            print("An error occurred:", e)

    def display_client_details(self):  # define a function to display client details in a table format by calling the ListClientForm
        # display the added client into the table that is created in the ListClientForm class
        ListClientForm(dt)

class ListClientForm:
    """Class to represent a GUI form to display data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('1200x400')  # set window size
        self.root.title("Client Details")  # set window title

        # Create the table to display all client details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Address', 'Contact', 'Budget', 'Events'), show='headings')
        # set column heading for each attribute of the client
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Contact', text='Contact')
        self.table.heading('Budget', text='Budget')
        self.table.heading('Events', text='Events')

        # Set column width for event to make sure all info is clearly displayed
        self.table.column('Events', width=1838)

        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_clients = self.data_layer.read_all_clients()
        for client_id, client in all_clients.items():
            # Insert client data into the table
            self.table.insert('', 'end', values=(client_id, client.get_name(), client.get_address(), client.get_contactDetails(), client.get_budget(), client.get_event()))
        self.root.mainloop()

class Client(Entity): # create a class for the client, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails, budget):  # define a constructor method to initialize the attributes of the Client class
        super().__init__(id, name, address, contactDetails) # call the attributes of the parent class
        self.__budget = budget
        self.__events = [] # create a list to store events associated with a client

    def set_budget(self, budget): # setter method for updating the budget
        self.__budget = budget

    def get_budget(self): # getter method for receiving the budget
        return self.__budget

    # implement a composition relationship between client and event
    def add_event(self, eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        self.__events.append(Event(eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice)) # add an event to the list

    def get_event(self): # getter method for receiving the event that a client has
        total_events=""
        for event in self.__events:
            total_events=str(event)
        return total_events

    def __str__(self): # define a function to display information about the Client
        return super().__str__() + f", Client Budget: {self.__budget}\nEvents to organize: {self.get_event()}"

class DataLayer:
    """Class to handle read and write operations for client data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_clients(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_clients = pickle.load(file)
                    return all_clients
        except Exception as e:
            print("An error occurred while reading client data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_clients_to_file(self, all_clients):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the clients data to the file
                pickle.dump(all_clients, f)
                print("Client data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing client data to file:", e)


# Create an instance of the DataLayer class
filename = "clients.pkl"
dt = DataLayer(filename)
# Create an instance of the ClientGUI class and pass the data_layer argument
client_gui = ClientGUI(dt)
# Read all clients from the data layer
all_clients = dt.read_all_clients()
# Create an instance of the ListClientForm class to display client details
show_client = ListClientForm(dt)
