from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class VenueGUI: # create a GUI class for the venue
    def __init__(self, data_layer):
        self.data_layer = data_layer  # Initialize data layer
        self.root = tk.Tk()  # Create a Tkinter root window
        self.root.geometry("500x500")  # Set window size
        self.root.title("Venue Management System")  # Set window title

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

        self.maxGuest_label = tk.Label(self.root, text="Max Guest:")  # create a label for Max Guest
        self.maxGuest_label.grid(row=4, column=0, sticky=tk.W, pady=5)  # place the Max Guest label in the grid
        self.maxGuest_entry = tk.Entry(self.root)  # create an entry field for Max Guest
        self.maxGuest_entry.grid(row=4, column=1)  # place the Max Guest entry field in the grid

        self.minGuest_label = tk.Label(self.root, text="Min Guest:")  # create a label for Min Guest
        self.minGuest_label.grid(row=5, column=0, sticky=tk.W, pady=5)  # place the Min Guest label in the grid
        self.minGuest_entry = tk.Entry(self.root)  # create an entry field for Min Guest
        self.minGuest_entry.grid(row=5, column=1)  # place the Min Guest entry field in the grid

        # Button to add venue details
        self.add_button = tk.Button(self.root, text="Add Venue", command=self.add_venue)
        self.add_button.grid(row=6, column=0, pady=5)

        # Button to delete certain venue details
        self.delete_button = tk.Button(self.root, text="Delete Venue", command=self.delete_venue)
        self.delete_button.grid(row=6, column=1, pady=5)

        # Button to modify certain venue details
        self.modify_button = tk.Button(self.root, text="Modify Venue", command=self.modify_venue)
        self.modify_button.grid(row=7, column=0, pady=5)

        # Button to display venue details in a table format
        self.display_button = tk.Button(self.root, text="Display Venue Details", command=self.display_venue_details)
        self.display_button.grid(row=7, column=1, pady=5)

        # Button to display events associated with a venue
        self.add_event_button = tk.Button(self.root, text="Add Event", command=self.add_venue_events)
        self.add_event_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.maxGuest_entry.delete(0, tk.END)
        self.minGuest_entry.delete(0, tk.END)


    def add_venue(self):  # define a function to add venue
        try:
            # Retrieve venue details from entry fields
            venue_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            max_guests = int(self.maxGuest_entry.get())
            min_guests = int(self.minGuest_entry.get())
            # create a Venue object
            venue = Venue(venue_id, name, address, contact_details, max_guests, min_guests)

            # Display the collected information
            print("Venue added successfully:")
            print("ID:", venue_id)
            print("Name:", name)
            print("Address:", address)
            print("Contact Details:", contact_details)
            print("Max Guests:", max_guests)
            print("Min Guests:", min_guests)

            # Retrieve existing venues from data layer to be able to check if ID already exists
            all_venues = self.data_layer.read_all_venues()

            # Check if ID already exists
            if venue_id in all_venues:
                # Display a message box informing the user that the venue with the given ID already exists
                tk.messagebox.showinfo("ID Check", f"The ID '{venue_id}' already exists for a venue.")
            else:
                all_venues[venue_id] = venue
                # Display a message box informing the user that the venue details was added successfully
                tk.messagebox.showinfo("Venue Added",f"The venue with ID '{venue_id}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_venues_to_file(all_venues)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)


    def delete_venue(self):  # define a function to delete a venue
        try:
            # Retrieve ID of Venue to delete
            venue_id = int(self.id_entry.get())
            # Retrieve existing venues from data layer
            all_venues = self.data_layer.read_all_venues()

            # Check if ID already exists
            if venue_id in all_venues:
                # Delete the venue
                del all_venues[venue_id]
                # Display a message box informing the user that the venue details was deleted successfully
                tk.messagebox.showinfo("Venue Deleted",f"The venue with ID '{venue_id}' has been deleted successfully.")
                # Write updated data to file
                self.data_layer.write_venues_to_file(all_venues)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the client with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The ID '{venue_id}' does not exist for a venue, do you want to add it?.")

        except Exception as e:
            print("An error occurred:", e)


    def modify_venue(self):  # define a function to modify a venue
        try:
            # Retrieve modified venue details from entry fields
            venue_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            address = str(self.address_entry.get())
            contact_details = int(self.contact_entry.get())
            max_guests = int(self.maxGuest_entry.get())
            min_guests = int(self.minGuest_entry.get())
            # create a Venue object
            venue = Venue(venue_id, name, address, contact_details, max_guests, min_guests)

            # Retrieve existing venues from data layer
            all_venues = self.data_layer.read_all_venues()

            # Check if ID already exists
            if venue_id in all_venues:
                # Update client details for a specified id
                all_venues[venue_id] = venue
                # Display a message box informing the user that the venue details was modified successfully
                tk.messagebox.showinfo("Venue Modified",f"The venue with ID '{venue_id}' has been modified successfully.")
                # Write updated data to file
                self.data_layer.write_venues_to_file(all_venues)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the client with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The venue with ID '{venue_id}' does not exist")

        except Exception as e:
            print("An error occurred:", e)

    def add_venue_events(self):  # define a function to add events associated with a venue
        try:
            # Retrieve the venue ID that you want to add the event to
            venue_id = int(self.id_entry.get())
            # Retrieve existing venues from data layer
            all_venues = self.data_layer.read_all_venues()
            # Check if the selected venue ID exists
            if venue_id in all_venues:
                venue = all_venues[venue_id]
                # create composition - add an event that will be placed in a certain venue
                venue.add_event(3, "Wedding", "Classic", "June 7", 1.00, "6 hours", "Emirates Palace", "It's Hafla Caterers", None, "Furniture for Wedding Inc.", "Musics", "Urbans of Spaces", None)
                # Write updated data to file
                self.data_layer.write_venues_to_file(all_venues)
                # Display a message box informing the user that the event was added to the venue successfully
                tk.messagebox.showinfo("Event Added", "Event added to the venue successfully.")
            else:
                # Display a message box informing the user that the venue with the given ID doesn't exist
                tk.messagebox.showinfo("Venue Not Found", f"The venue with ID '{venue_id}' does not exist.")

        except Exception as e:
            print("An error occurred:", e)

    def display_venue_details(self):  # define a function to display venue details in a table format by calling the ListVenueForm
        # display the added venue into the table created in the ListVenueForm class
        ListVenueForm(dt)


class ListVenueForm:
    """Class to represent a GUI form to display data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('1200x400')  # set window size
        self.root.title("Venue Details")  # set window title

        # Create the table to display all venue details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Address', 'Contact', 'Max Guests', 'Min Guests', 'Events'), show='headings')
        # set column heading for each attribute of the venue
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Contact', text='Contact')
        self.table.heading('Max Guests', text='Max Guests')
        self.table.heading('Min Guests', text='Min Guests')
        self.table.heading('Events', text='Events')

        # Set column width for event to make sure all info is clearly displayed
        self.table.column('Events', width=1977)

        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_venues = self.data_layer.read_all_venues()
        for venue_id, venue in all_venues.items():
            # Insert venue data into the table
            self.table.insert('', 'end', values=(venue_id, venue.get_name(), venue.get_address(), venue.get_contactDetails(), venue.get_maxGuests(), venue.get_minGuests(), venue.get_event()))

        self.root.mainloop()


class Venue(Entity): # create a class for the venue, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails, maxGuests, minGuests):  # define a constructor method to initialize the attributes of the Venue class
        super().__init__(id, name, address, contactDetails)  # call the attributes of the parent class
        self.__maxGuests = maxGuests
        self.__minGuests = minGuests
        self.__events = [] # create a list to store events associated with a venue

    def set_maxGuests(self, maxGuests): # setter method for updating the maximum number of guests
        self.__maxGuests = maxGuests

    def set_minGuests(self, minGuests): # setter method for updating the minimum number of guests
        self.__minGuests = minGuests

    def get_maxGuests(self): # getter method for receiving the maximum number of guests
        return self.__maxGuests

    def get_minGuests(self): # getter method for receiving the minimum number of guests
        return self.__minGuests

    # implement a composition relationship between venue and event
    def add_event(self, eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        self.__events.append(Event(eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice)) # add event to the list

    def get_event(self): # getter method for receiving the event that a venue has
        total_events=""
        for event in self.__events:
            total_events=str(event)
        return total_events

    def __str__(self): # define a function to display information about the Supplier
        return super().__str__() + f", Venue Maximum Guests: {self.__maxGuests}, Venue Minimum Guests: {self.__minGuests}\nEvent Hosted: {self.get_event()}"


class DataLayer:
    """Class to handle read and write operations for venue data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_venues(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_venues = pickle.load(file)
                    return all_venues
        except Exception as e:
            print("An error occurred while reading venue data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_venues_to_file(self, all_venues):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the venue data to the file
                pickle.dump(all_venues, f)
                print("Venue data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing venue data to file:", e)


# Create an instance of the DataLayer class
filename = "venue.pkl"
dt = DataLayer(filename)
# Create an instance of the VenueGUI class and pass the data_layer argument
venue_gui = VenueGUI(dt)
# Read all venue from the data layer
all_venues = dt.read_all_venues()
# Create an instance of the ListClientForm class to display venue details
show_venue = ListVenueForm(dt)