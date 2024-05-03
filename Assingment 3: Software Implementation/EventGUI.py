from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class EventGUI:  # create a GUI class for the event
    def __init__(self, data_layer):
        self.data_layer = data_layer  # Initialize data layer
        self.root = tk.Tk()  # Create a Tkinter root window
        self.root.geometry("600x600")  # Set window size
        self.root.title("Event Management System")  # Set window title

        # Labels and Entry fields
        self.id_label = tk.Label(self.root, text="ID:")  # create a label for ID
        self.id_label.grid(row=0, column=0, sticky=tk.W, pady=5)  # place the ID label in the grid
        self.id_entry = tk.Entry(self.root)  # create an entry field for ID
        self.id_entry.grid(row=0, column=1)  # place the ID entry field in the grid

        self.type_label = tk.Label(self.root, text="Type:")  # create a label for Type
        self.type_label.grid(row=1, column=0, sticky=tk.W, pady=5)  # place the Type label in the grid
        self.type_entry = tk.Entry(self.root)  # create an entry field for Type
        self.type_entry.grid(row=1, column=1)  # place the Type entry field in the grid

        self.theme_label = tk.Label(self.root, text="Theme:")  # create a label for Theme
        self.theme_label.grid(row=2, column=0, sticky=tk.W, pady=5)  # place the Theme label in the grid
        self.theme_entry = tk.Entry(self.root)  # create an entry field for Theme
        self.theme_entry.grid(row=2, column=1)  # place the Theme entry field in the grid

        self.date_label = tk.Label(self.root, text="Date:")  # create a label for Date
        self.date_label.grid(row=3, column=0, sticky=tk.W, pady=5)  # place the Date label in the grid
        self.date_entry = tk.Entry(self.root)  # create an entry field for Date
        self.date_entry.grid(row=3, column=1)  # place the Date entry field in the grid

        self.time_label = tk.Label(self.root, text="Time:")  # create a label for Time
        self.time_label.grid(row=4, column=0, sticky=tk.W, pady=5)  # place the Time label in the grid
        self.time_entry = tk.Entry(self.root)  # create an entry field for Time
        self.time_entry.grid(row=4, column=1)  # place the Time entry field in the grid

        self.duration_label = tk.Label(self.root, text="Duration:")  # create a label for Duration
        self.duration_label.grid(row=5, column=0, sticky=tk.W, pady=5)  # place the Duration label in the grid
        self.duration_entry = tk.Entry(self.root)  # create an entry field for Duration
        self.duration_entry.grid(row=5, column=1)  # place the Duration entry field in the grid

        self.address_label = tk.Label(self.root, text="Venue Address:")  # create a label for Venue Address
        self.address_label.grid(row=6, column=0, sticky=tk.W, pady=5)    # place the Venue Address label in the grid
        self.address_entry = tk.Entry(self.root)  # create an entry field for Venue Address
        self.address_entry.grid(row=6, column=1)  # place the Venue Address entry field in the grid

        self.catering_label = tk.Label(self.root, text="Catering Company:")  # create a label for Catering Company
        self.catering_label.grid(row=7, column=0, sticky=tk.W, pady=5)  # place the Catering Company label in the grid
        self.catering_entry = tk.Entry(self.root)  # create an entry field for Catering Company
        self.catering_entry.grid(row=7, column=1)  # place the Catering Company entry field in the grid

        self.cleaning_label = tk.Label(self.root, text="Cleaning Company:")  # create a label for Cleaning Company
        self.cleaning_label.grid(row=8, column=0, sticky=tk.W, pady=5)  # place the Cleaning Company label in the grid
        self.cleaning_entry = tk.Entry(self.root)  # create an entry field for Cleaning Company
        self.cleaning_entry.grid(row=8, column=1)  # place the Cleaning Company entry field in the grid

        self.decorations_label = tk.Label(self.root, text="Decorations Company:")  # create a label for Decorations Company
        self.decorations_label.grid(row=9, column=0, sticky=tk.W, pady=5)  # place the Decorations Company label in the grid
        self.decorations_entry = tk.Entry(self.root)  # create an entry field for Decorations Company
        self.decorations_entry.grid(row=9, column=1)  # place the Decorations Company entry field in the grid

        self.entertainment_label = tk.Label(self.root, text="Entertainment Company:")  # create a label for Entertainment Company
        self.entertainment_label.grid(row=10, column=0, sticky=tk.W, pady=5)  # place the Entertainment Company label in the grid
        self.entertainment_entry = tk.Entry(self.root)  # create an entry field for Entertainment Company
        self.entertainment_entry.grid(row=10, column=1)  # place the Entertainment Company entry field in the grid

        self.furniture_label = tk.Label(self.root, text="Furniture Supply Company:")  # create a label for Furniture Supply Company
        self.furniture_label.grid(row=11, column=0, sticky=tk.W, pady=5)  # place the Furniture Supply Company label in the grid
        self.furniture_entry = tk.Entry(self.root)  # create an entry field for Furniture Supply Company
        self.furniture_entry.grid(row=11, column=1)  # place the Furniture Supply Company entry field in the grid

        self.invoice_label = tk.Label(self.root, text="Invoice:")  # create a label for Invoice
        self.invoice_label.grid(row=12, column=0, sticky=tk.W, pady=5)  # place the Invoice label in the grid
        self.invoice_entry = tk.Entry(self.root)  # create an entry field for Invoice
        self.invoice_entry.grid(row=12, column=1)  # place the Invoice entry field in the grid

        # Button to add event details
        self.add_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.add_button.grid(row=13, column=0, pady=5)

        # Button to delete certain event details
        self.delete_button = tk.Button(self.root, text="Delete Event", command=self.delete_event)
        self.delete_button.grid(row=13, column=1, pady=5)

        # Button to modify certain event details
        self.modify_button = tk.Button(self.root, text="Modify Event", command=self.modify_event)
        self.modify_button.grid(row=14, column=0, pady=5)

        # Button to display event details in a table format
        self.display_button = tk.Button(self.root, text="Display Event Details", command=self.display_event_details)
        self.display_button.grid(row=14, column=1, pady=5)

        # Button to display guests associated with an event
        self.display_button = tk.Button(self.root, text="Add Guests", command=self.add_guests)
        self.display_button.grid(row=15, column=0, columnspan=2, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.theme_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.catering_entry.delete(0, tk.END)
        self.cleaning_entry.delete(0, tk.END)
        self.decorations_entry.delete(0, tk.END)
        self.entertainment_entry.delete(0, tk.END)
        self.furniture_entry.delete(0, tk.END)
        self.invoice_entry.delete(0, tk.END)

    def add_event(self):  # define a function to add events
        try:
            # Retrieve event details from entry fields
            eventID = int(self.id_entry.get())
            eventType = str(self.type_entry.get())
            eventTheme = str(self.theme_entry.get())
            eventDate = str(self.date_entry.get())
            eventTime = str(self.time_entry.get())
            eventDuration = str(self.duration_entry.get())
            venueAddress = str(self.address_entry.get())
            cateringCompany = str(self.catering_entry.get())
            cleaningCompany = str(self.cleaning_entry.get())
            decorationsCompany = str(self.decorations_entry.get())
            entertainmentCompany = str(self.entertainment_entry.get())
            furnitureSupplyCompany = str(self.furniture_entry.get())
            invoice = str(self.invoice_entry.get())
            # Create an Event object
            event = Event(eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice)

            # Display the collected information
            print("Event added successfully:")
            print("ID:", eventID)
            print("Type:", eventType)
            print("Theme:", eventTheme)
            print("Date:", eventDate)
            print("Time:", eventTime)
            print("Duration:", eventDuration)
            print("Address:", venueAddress)
            print("Catering Company:", cateringCompany)
            print("Cleaning Company:", cleaningCompany)
            print("Decoration Company:", decorationsCompany)
            print("Entertainment Company:", entertainmentCompany)
            print("Furniture Supply Company:", furnitureSupplyCompany)
            print("Invoice:", invoice)

            # Retrieve existing events from data layer
            all_events = self.data_layer.read_all_events()

            # Check if event ID already exists
            if eventID in all_events:
                # Display a message box informing the user that the event with the given ID already exists
                tkinter.messagebox.showinfo("ID Check", f"The ID '{eventID}' already exists for an event.")
            else:
                all_events[eventID] = event
                # Display a message box informing the user that the event details was added successfully
                tkinter.messagebox.showinfo("Event Added",f"The event with ID '{eventID}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_events_to_file(all_events)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)

    def delete_event(self):  # define a function to delete event details
        try:
            # Retrieve ID of Event to delete
            eventID = int(self.id_entry.get())
            # Retrieve existing events from data layer
            all_events = self.data_layer.read_all_events()

            # Check if ID already exists
            if eventID in all_events:
                # Delete the event
                del all_events[eventID]
                # Display a message box informing the user that the events details was deleted successfully
                tk.messagebox.showinfo("Event Deleted",f"The event with ID '{eventID}' has been deleted successfully")
                # Write updated data to file
                self.data_layer.write_events_to_file(all_events)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the event with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The event with ID '{eventID}' does not exist")

        except Exception as e:
            print("An error occurred:", e)

    def modify_event(self):  # define a function to modify event details
        try:
            # Retrieve modified event details from entry fields
            eventID = int(self.id_entry.get())
            eventType = str(self.type_entry.get())
            eventTheme = str(self.theme_entry.get())
            eventDate = str(self.date_entry.get())
            eventTime = str(self.time_entry.get())
            eventDuration = str(self.duration_entry.get())
            venueAddress = str(self.address_entry.get())
            cateringCompany = str(self.catering_entry.get())
            cleaningCompany = str(self.cleaning_entry.get())
            decorationsCompany = str(self.decorations_entry.get())
            entertainmentCompany = str(self.entertainment_entry.get())
            furnitureSupplyCompany = str(self.furniture_entry.get())
            invoice = str(self.invoice_entry.get())
            # create an Event object
            event = Event(eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice)

            # Retrieve existing events from data layer
            all_events = self.data_layer.read_all_events()

            # Check if ID already exists
            if eventID in all_events:
                all_events[eventID] = event
                # Display a message box informing the user that the event details was modified successfully
                tk.messagebox.showinfo("Event Modified",f"The event with ID '{eventID}' has been modified successfully.")
                # Write updated data to file
                self.data_layer.write_events_to_file(all_events)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the event with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The ID '{eventID}' does not exist for a event, do you want to add it?.")

        except Exception as e:
            print("An error occurred:", e)


    def add_guests(self):  # define a function to add guests associated with an event
        try:
            # Retrieve the event ID that you want to add the guest to
            event_id = int(self.id_entry.get())
            # Retrieve existing events from data layer
            all_events = self.data_layer.read_all_events()
            # Check if the selected event ID exists
            if event_id in all_events:
                event = all_events[event_id]
                # create an aggregation - adding guests associated with an event
                event.add_guests(2, "Khalid", "Mushrif St", 559384500, "VIP")

                # Write updated data to file
                self.data_layer.write_events_to_file(all_events)
                # Display a message box informing the user that the guest was added to the event successfully
                tk.messagebox.showinfo("Guest Added", "Guest added to the event successfully.")
            else:
                # Display a message box informing the user that the event with the given ID doesn't exist
                tk.messagebox.showinfo("Event Not Found", f"The event with ID '{event_id}' does not exist.")

        except Exception as e:
             print("An error occurred:", e)

    def display_event_details(self):  # define a function to display event details in a table format by calling the ListEventForm
        # display the added event into the table created in the ListEventForm class
        ListEventForm(dt)

class ListEventForm:
    """Class to represent a GUI form to display event data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('1400x400')  # set window size
        self.root.title("Event Details")  # set window title

        # Create the table to display all event details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Type', 'Theme', 'Date', 'Time', 'Duration', 'Venue Address', 'Catering Company', 'Cleaning Company', 'Decoration Company', 'Entertainment Company', 'Furniture Supply Company', 'Invoice', 'Guests'), show='headings')
        # set column heading for each attribute of the event
        self.table.heading('ID', text='ID')
        self.table.heading('Type', text='Type')
        self.table.heading('Theme', text='Theme')
        self.table.heading('Date', text='Date')
        self.table.heading('Time', text='Time')
        self.table.heading('Duration', text='Duration')
        self.table.heading('Venue Address', text='Venue Address')
        self.table.heading('Catering Company', text='Catering Company')
        self.table.heading('Cleaning Company', text='Cleaning Company')
        self.table.heading('Decoration Company', text='Decoration Company')
        self.table.heading('Entertainment Company', text='Entertainment Company')
        self.table.heading('Furniture Supply Company', text='Furniture Supply Company')
        self.table.heading('Invoice', text='Invoice')
        self.table.heading('Guests', text='Guests')

        # Set column width for event to make sure all info is clearly displayed
        self.table.column('Guests', width=600)

        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_event = self.data_layer.read_all_events()
        for eventID, event in all_event.items():
            # Insert event data into the table
            self.table.insert('', 'end', values=(eventID, event.get_eventType(), event.get_eventTheme(), event.get_eventDate(), event.get_eventTime(), event.get_eventDuration(), event.get_venueAddress(), event.get_cateringCompany(), event.get_cleaningCompany(), event.get_decorationsCompany(), event.get_entertainmentCompany(), event.get_furnitureSupplyCompany(), event.get_invoice(), event.get_guests()))

        self.root.mainloop()

class Event: # create a class for the event
    def __init__(self, eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice): # define a constructor method to initialize the attributes of the Event class
        self.__eventID = eventID
        self.__eventType = eventType
        self.__eventTheme = eventTheme
        self.__eventDate = eventDate
        self.__eventTime = eventTime
        self.__eventDuration = eventDuration
        self.__venueAddress = venueAddress
        self.__cateringCompany = cateringCompany
        self.__cleaningCompany = cleaningCompany
        self.__decorationsCompany = decorationsCompany
        self.__entertainmentCompany = entertainmentCompany
        self.__furnitureSupplyCompany = furnitureSupplyCompany
        self.__invoice = invoice
        self.__employees = [] # create a list to store employees associated with a specific event
        self.__guest = [] # create a list to store guests associated with a specific event
        self.__supplier = [] # create a list to store suppliers associated with a specific event
        self.__caterer = [] # create a list to store caterers associated with a specific event

    def set_eventID(self, eventID): # setter method for updating the event id
        self.__eventID = eventID

    def set_eventType(self, eventType): # setter method for updating the event type
        self.__eventType = eventType

    def set_eventTheme(self, eventTheme): # setter method for updating the event theme
        self.__eventTheme = eventTheme

    def set_eventDate(self, eventDate): # setter method for updating the event date
        self.__eventDate = eventDate

    def set_eventTime(self, eventTime): # setter method for updating the event time
        self.__eventTime = eventTime

    def set_eventDuration(self, eventDuration): # setter method for updating the event duration
        self.__eventDuration = eventDuration

    def set_venueAddress(self, venueAddress): # setter method for updating the catering company
        self.__venueAddress = venueAddress

    def set_cateringCompany(self, cateringCompany): # setter method for updating the maximum number of guests
        self.__cateringCompany = cateringCompany

    def set_cleaningCompany(self, cleaningCompany): # setter method for updating the cleaning company
        self.__cleaningCompany = cleaningCompany

    def set_decorationsCompany(self, decorationsCompany): # setter method for updating the decorations company
        self.__decorationsCompany = decorationsCompany

    def set_entertainmentCompany(self, entertainmentCompany): # setter method for updating the entertainment company
        self.__entertainmentCompany = entertainmentCompany

    def set_furnitureSupplyCompany(self, furnitureSupplyCompany): # setter method for updating the furniture supply company
        self.__furnitureSupplyCompany = furnitureSupplyCompany

    def set_invoice(self, invoice): # setter method for updating the invoice
        self.__invoice = invoice

    def get_eventID(self): # getter method for receiving the event id
        return self.__eventID

    def get_eventType(self): # getter method for receiving the event type
        return self.__eventType

    def get_eventTheme(self): # getter method for receiving the event theme
        return self.__eventTheme

    def get_eventDate(self): # getter method for receiving the event date
        return self.__eventDate

    def get_eventTime(self): # getter method for receiving the event time
        return self.__eventTime

    def get_eventDuration(self): # getter method for receiving the event duration
        return self.__eventDuration

    def get_venueAddress(self): # getter method for receiving the venue address
        return self.__venueAddress

    def get_cateringCompany(self): # getter method for receiving the catering company
        return self.__cateringCompany

    def get_cleaningCompany(self): # getter method for receiving the cleaning company
        return self.__cleaningCompany

    def get_decorationsCompany(self): # getter method for receiving the decorations company
        return self.__decorationsCompany

    def get_entertainmentCompany(self): # getter method for receiving the entertainment company
        return self.__entertainmentCompany

    def get_furnitureSupplyCompany(self): # getter method for receiving the furniture supply company
        return self.__furnitureSupplyCompany

    def get_invoice(self): # getter method for receiving the minimum invoice
        return self.__invoice

    # implementing a unary association relationship between event and employees
    def add_employees(self, employees):
        self.__employees.append(employees) # add employee to the list

    def get_employees(self): #getter method for receiving the employees that an event has
        print(f"The event with ID {self.get_eventID()} employees:")
        for employee in self.__employees:
            print(employee)

    # implementing an aggregation relationship between event and supplier
    def add_supplier(self, supplier):
        self.__supplier.append(supplier) # add supplier to the list

    def get_suppliers(self): # getter method for receiving the supplier that an event has
        total_supplier = ""
        for supplier in self.__supplier:
            total_supplier+=str(supplier)
        return total_supplier

    # implementing an aggregation relationship between event and caterer
    def add_caterer(self, caterer):
        self.__caterer.append(caterer) # add caterer to the list

    def get_caterer(self): # getter method for receiving the caterer that an event has
        total_caterer = ""
        for caterer in self.__caterer:
            total_caterer+=str(caterer)
        return total_caterer

    # implementing a composition relationship between event and guests
    def add_guests(self, id, name, address, contactDetails, status):
        self.__guest.append(Guest(id, name, address, contactDetails, status)) # add guest to the list

    def get_guests(self): # getter method for receiving the guest that an event has
        total_guests = ""
        for guest in self.__guest:
            total_guests+=str(guest)
        return total_guests

    def __str__(self): # define a function to display information about the Event
        return f"ID: {self.__eventID}, Type: {self.__eventType}, Theme: {self.__eventTheme}, Date: {self.__eventDate}, Time: {self.__eventTime}, Duration: {self.__eventDuration}, Venue Address: {self.__venueAddress}, Catering Company: {self.__cateringCompany}, Cleaning Company: {self.__cleaningCompany}, Decorations Company: {self.__decorationsCompany}, Entertainment Company: {self.__entertainmentCompany}, Furniture Supply Company: {self.__furnitureSupplyCompany}, Invoice: {self.__invoice}\nSuppliers: {self.get_suppliers()}\nCaterers: {self.get_caterer()}\nGuests: {self.get_guests()}"

class DataLayer:
    """Class to handle read and write operations for event data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_events(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_events = pickle.load(file)
                    return all_events
        except Exception as e:
            print("An error occurred while reading event data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_events_to_file(self, all_events):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the event data to the file
                pickle.dump(all_events, f)
                print("Event data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing event data to file:", e)


# Create an instance of the DataLayer class
filename = "event.pkl"
dt = DataLayer(filename)
# Create an instance of the EventGUI class and pass the data_layer argument
event_gui = EventGUI(dt)
# Read all events from the data layer
all_events = dt.read_all_events()
# Create an instance of the ListEventForm class to display event details
show_event = ListEventForm(dt)