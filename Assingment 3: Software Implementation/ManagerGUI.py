from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class ManagerGUI: # create a GUI class for the manager
    def __init__(self, data_layer):
        self.data_layer = data_layer  # Initialize data layer
        self.root = tk.Tk()  # Create a Tkinter root window
        self.root.geometry("400x350")  # Set window size
        self.root.title("Manager Management System")  # Set window title

        # Labels and Entry fields
        self.id_label = tk.Label(self.root, text="ID:")  # create a label for ID
        self.id_label.grid(row=0, column=0, sticky=tk.W, pady=5)  # place the ID label in the grid
        self.id_entry = tk.Entry(self.root)  # create an entry field for ID
        self.id_entry.grid(row=0, column=1)  # place the ID entry field in the grid

        self.name_label = tk.Label(self.root, text="Name:")  # create a label for Name
        self.name_label.grid(row=1, column=0, sticky=tk.W, pady=5)  # place the Name label in the grid
        self.name_entry = tk.Entry(self.root)  # create an entry field for Name
        self.name_entry.grid(row=1, column=1)  # place the Name entry field in the grid

        # Button to add manager details
        self.add_button = tk.Button(self.root, text="Add Manager", command=self.add_manager)
        self.add_button.grid(row=2, column=0, pady=10)

        # Button to delete certain manager details
        self.delete_button = tk.Button(self.root, text="Delete Manager", command=self.delete_manager)
        self.delete_button.grid(row=2, column=1, pady=10)

        # Button to modify certain manager details
        self.modify_button = tk.Button(self.root, text="Modify Manager", command=self.modify_manager)
        self.modify_button.grid(row=3, column=0, pady=10)

        # Button to display manager details in a table format
        self.display_button = tk.Button(self.root, text="Display Manager Details", command=self.display_manager_details)
        self.display_button.grid(row=3, column=1, pady=10)

        # Button to display employees associated with a manager
        self.add_employees_button = tk.Button(self.root, text="Add Employee", command=self.add_employees)
        self.add_employees_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)

    def add_manager(self):  # define a function to add manager
        try:
            # Retrieve manager details from entry fields
            managerID = int(self.id_entry.get())
            name = str(self.name_entry.get())

            # Display the collected information
            print("Caterer added successfully:")
            print("ID:", managerID)
            print("Name:", name)
            # create a Manager object
            manager = Manager(managerID, name)

            # Retrieve existing managers from data layer
            all_managers = self.data_layer.read_all_managers()

            # Check if ID already exists
            if managerID in all_managers:
                # Display a message box informing the user that the manager with the given ID already exists
                tk.messagebox.showinfo("ID Check", f"The ID '{managerID}' already exists for a manager.")
            else:
                all_managers[managerID] = manager
                # Display a message box informing the user that the manager details was added successfully
                tk.messagebox.showinfo("Manager Added",f"The manager with ID '{managerID}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_managers_to_file(all_managers)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)

    def delete_manager(self):  # define a function to delete manager details
        try:
            # Retrieve ID of manager to delete
            managerID = int(self.id_entry.get())
            # Retrieve existing managers from data layer
            all_managers = self.data_layer.read_all_managers()

            # Check if ID already exists
            if managerID in all_managers:
                # Delete the manager
                del all_managers[managerID]
                # Display a message box informing the user that the managers details was deleted successfully
                tk.messagebox.showinfo("Manager Deleted",f"The manager with ID '{managerID}' has been deleted successfully.")
                # Write updated data to file
                self.data_layer.write_managers_to_file(all_managers)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the manager with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The ID '{managerID}' does not exist for a manager, do you want to add it?")

        except Exception as e:
            print("An error occurred:", e)

    def modify_manager(self):  # define a function to modify manager details
        try:
            # Retrieve modified manager details from entry fields
            managerID = int(self.id_entry.get())
            name = str(self.name_entry.get())
            # create a Manager object
            manager = Manager(managerID, name)

            # Retrieve existing manager from data layer
            all_managers = self.data_layer.read_all_managers()

            # Check if ID already exists
            if managerID in all_managers:
                all_managers[managerID] = manager
                # Display a message box informing the user that the manager details was modified successfully
                tk.messagebox.showinfo("Manager Modified", f"The manager with ID '{managerID}' has been modified successfully.")
                # Write updated data to file
                self.data_layer.write_managers_to_file(all_managers)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the manager with the given ID doesn't exist
                tk.messagebox.showinfo("ID Check", f"The manager with ID '{managerID}' does not exist")

        except Exception as e:
            print("An error occurred:", e)

    def add_employees(self):  # define a function to add employees associated with a specific manager
        try:
            # Retrieve the manager ID that you want to add the employee to
            managerID = int(self.id_entry.get())
            # Retrieve existing managers from data layer
            all_manager = self.data_layer.read_all_managers()
            # Check if the selected manager ID exists
            if managerID in all_manager:
                manager = all_manager[managerID]
                # create an aggregation - adding employees managed by a certain manager
                employee = Employee("Mohammed", 3, "Designer", "DesignLeader", 45000, 25, "1999-05-27", "SDF678", EmployeeType.Designer)
                manager.add_employees(employee)
                # Write updated data to file
                self.data_layer.write_managers_to_file(all_manager)
                # Display a message box informing the user that the employee was added to the manager successfully
                tk.messagebox.showinfo("Employee Added", "Employee added to the manager successfully.")
            else:
                # Display a message box informing the user that the manager with the given ID doesn't exist
                tk.messagebox.showinfo("Manager Not Found", f"The manager with ID '{managerID}' does not exist.")

        except Exception as e:
             print("An error occurred:", e)

    def display_manager_details(self): # define a function to display manager details in a table format by calling the ListMangerForm
        # display the added manager into the table created in the ListManagerForm class
        ListManagerForm(dt)


class ListManagerForm:
    """Class to represent a GUI form to display data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('1400x400')  # set window size
        self.root.title("Manager Details")  # set window title

        # Create the table to display all manager details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Employees Managed'), show='headings')
        # set column heading for each attribute of the manager
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Employees Managed', text='Employees Managed')

        # Set column widths for each attribute
        self.table.column('ID', width=100)
        self.table.column('Name', width=150)
        self.table.column('Employees Managed', width=1200)

        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_manager = self.data_layer.read_all_managers()
        for managerID, manager in all_manager.items():
            # Insert manager data into the table
            self.table.insert('', 'end', values=(managerID, manager.get_managerName(), manager.get_employees()))

        self.root.mainloop()


class Manager: # create a class for a manager
    def __init__(self, managerID, managerName):  # define a constructor method to initialize the attributes of the Event class
        self.__managerID = managerID
        self.__managerName = managerName
        self.__employees = [] # create a list to store employees associated with a manager

    def set_managerID(self, manageriD): # setter method for updating the manager id
        self.__managerID = manageriD

    def set_managerName(self, managerName): # setter method for updating the manager name
        self.__managerName = managerName

    def get_managerID(self): # getter method for receiving the manager id
        return self.__managerID

    def get_managerName(self): # getter method for receiving the manager name
        return self.__managerName

    # implementing an aggregation relationship between Manager and Employees
    def add_employees(self, employee):
        self.__employees.append(employee) # add employee to the list

    def get_employees(self): # getter method for receiving the list of employees that are managed by a certain manager
        total_employees=""
        for employee in self.__employees:
            total_employees+=str(employee)
        return total_employees

    def __str__(self): # define a function to display information about the manager with its associated employees
        return f"Manager ID: {self.__managerID}, Manager Name: {self.__managerName}\nList of Managed Employees:\n{self.get_employees()}"


class DataLayer:
    """Class to handle read and write operations for manager data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_managers(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_managers = pickle.load(file)
                    return all_managers
        except Exception as e:
            print("An error occurred while reading manager data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_managers_to_file(self, all_managers):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the manager data to the file
                pickle.dump(all_managers, f)
                print("Manager data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing manager data to file:", e)


# Create an instance of the DataLayer class
filename = "manager.pkl"
dt = DataLayer(filename)
# Create an instance of the ManagerGUI class and pass the data_layer argument
manager_gui = ManagerGUI(dt)
# Read all managers from the data layer
all_manager = dt.read_all_managers()
# Create an instance of the ListManagerForm class to display manager details
show_manager = ListManagerForm(dt)