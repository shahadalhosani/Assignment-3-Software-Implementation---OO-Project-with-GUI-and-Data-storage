from Classes import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pickle
import os

class EmployeeGUI:   # create a GUI class for the employee
    def __init__(self, data_layer):
        self.data_layer = data_layer  # Initialize data layer
        self.root = tk.Tk()  # Create a Tkinter root window
        self.root.geometry("500x500")  # Set window size
        self.root.title("Employee Management System")  # Set window title

        # Labels and Entry fields
        self.id_label = tk.Label(self.root, text="ID:")   # create a label for ID
        self.id_label.grid(row=0, column=0, sticky=tk.W, pady=5)  # place the ID label in the grid
        self.id_entry = tk.Entry(self.root)  # create an entry field for ID
        self.id_entry.grid(row=0, column=1)  # place the ID entry field in the grid

        self.name_label = tk.Label(self.root, text="Name:")   # create a label for Name
        self.name_label.grid(row=1, column=0, sticky=tk.W, pady=5)  # place the Name label in the grid
        self.name_entry = tk.Entry(self.root)  # create an entry field for Name
        self.name_entry.grid(row=1, column=1)  # place the Name entry field in the grid

        self.department_label = tk.Label(self.root, text="Department:")   # create a label for Department
        self.department_label.grid(row=2, column=0, sticky=tk.W, pady=5)  # place the Department label in the grid
        self.department_entry = tk.Entry(self.root)  # create an entry field for Department
        self.department_entry.grid(row=2, column=1)  # place the Department entry field in the grid

        self.jobTitle_label = tk.Label(self.root, text="Job Title:")   # create a label for Job Title
        self.jobTitle_label.grid(row=3, column=0, sticky=tk.W, pady=5)  # place the Job Title label in the grid
        self.jobTitle_entry = tk.Entry(self.root)  # create an entry field for Job Title
        self.jobTitle_entry.grid(row=3, column=1)  # place the Job Title entry field in the grid

        self.basicSalary_label = tk.Label(self.root, text="Basic Salary:")   # create a label for Basic Salary
        self.basicSalary_label.grid(row=4, column=0, sticky=tk.W, pady=5)  # place the Basic Salary label in the grid
        self.basicSalary_entry = tk.Entry(self.root)  # create an entry field for Basic Salary
        self.basicSalary_entry.grid(row=4, column=1)  # place the Basic Salary entry field in the grid

        self.age_label = tk.Label(self.root, text="Age:")   # create a label for Age
        self.age_label.grid(row=5, column=0, sticky=tk.W, pady=5)  # place the Age label in the grid
        self.age_entry = tk.Entry(self.root)  # create an entry field for Age
        self.age_entry.grid(row=5, column=1)  # place the Age entry field in the grid

        self.dateOfBirth_label = tk.Label(self.root, text="Date of Birth:")   # create a label for Date of Birth
        self.dateOfBirth_label.grid(row=6, column=0, sticky=tk.W, pady=5)  # place the Date of Birth label in the grid
        self.dateOfBirth_entry = tk.Entry(self.root)  # create an entry field for Date of Birth
        self.dateOfBirth_entry.grid(row=6, column=1)  # place the Date of Birth entry field in the grid

        self.passportDetails_label = tk.Label(self.root, text="Passport Details:")   # create a label for Passport Details
        self.passportDetails_label.grid(row=7, column=0, sticky=tk.W, pady=5)  # place the Passport Details label in the grid
        self.passportDetails_entry = tk.Entry(self.root)  # create an entry field for Passport Details
        self.passportDetails_entry.grid(row=7, column=1)  # place the Passport Details entry field in the grid

        self.employeeType_label = tk.Label(self.root, text="Employee Type:")   # create a label for Employee Type
        self.employeeType_label.grid(row=8, column=0, sticky=tk.W, pady=5)  # place the Employee Type label in the grid
        self.employeeType_entry = tk.Entry(self.root)  # create an entry field for Employee Type
        self.employeeType_entry.grid(row=8, column=1)  # place the Employee Type entry field in the grid

        # Button to add employee details
        self.add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=9, column=0, pady=5)

        # Button to delete certain employee details
        self.delete_button = tk.Button(self.root, text="Delete Employee", command=self.delete_employee)
        self.delete_button.grid(row=9, column=1, pady=5)

        # Button to modify certain employee details
        self.modify_button = tk.Button(self.root, text="Modify Employee", command=self.modify_employee)
        self.modify_button.grid(row=10, column=0, pady=5)

        # Button to display employee details in a table format
        self.display_button = tk.Button(self.root, text="Display Employee Details", command=self.display_employee_details)
        self.display_button.grid(row=10, column=1, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        # Clear the Entry Box
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.jobTitle_entry.delete(0, tk.END)
        self.basicSalary_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.dateOfBirth_entry.delete(0, tk.END)
        self.passportDetails_entry.delete(0, tk.END)
        self.employeeType_entry.delete(0, tk.END)

    def add_employee(self):  # define a function to add employee details
        try:
            # Retrieve employee details from entry fields
            employee_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            department = str(self.department_entry.get())
            job_title = str(self.jobTitle_entry.get())
            basic_salary = float(self.basicSalary_entry.get())
            age = int(self.age_entry.get())
            date_of_birth = str(self.dateOfBirth_entry.get())
            passport_details = str(self.passportDetails_entry.get())
            employee_type = EmployeeType(self.employeeType_entry.get())
            # create an Employee object
            employee = Employee(employee_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, employee_type)

            # Display the collected information
            print("Employee added successfully:")
            print("ID:", employee_id)
            print("Name:", name)
            print("Department:", department)
            print("Job Title:", job_title)
            print("Basic Salary:", basic_salary)
            print("Age:", age)
            print("Date of Birth:", date_of_birth)
            print("Passport Details:", passport_details)
            print("Employee Type:", employee_type)

            # Retrieve existing employees from data layer
            all_employees = self.data_layer.read_all_employee()

            # Check if ID already exists
            if employee_id in all_employees:
                # Display a message box informing the user that the employee with the given ID already exists
                tk.messagebox.showinfo("ID Check", f"The ID '{employee_id}' already exists for an employee.")
            else:
                all_employees[employee_id] = employee
                # Display a message box informing the user that the employee details was added successfully
                tk.messagebox.showinfo("Employee Added",f"The employee with ID '{employee_id}' has been added successfully.")
                # Write updated data to file
                self.data_layer.write_employee_to_file(all_employees)
                # Clear entry boxes
                self.clearBoxes()

        except Exception as e:
            # Handle any exceptions that occur during retrieval or printing
            print("An error occurred:", e)

    def delete_employee(self):  # define a function to delete employee details
        try:
            # Retrieve employee ID to delete
            employee_id = int(self.id_entry.get())
            # Retrieve existing employees from data layer
            all_employees = self.data_layer.read_all_employee()

            # Check if the employee ID exists
            if employee_id in all_employees:
                # Delete the employee from the dictionary
                del all_employees[employee_id]
                # Display a message box informing the user that the employee details was deleted successfully
                tk.messagebox.showinfo("Employee Deleted", f"The employee with ID '{employee_id}' has been deleted successfully")
                # Write updated data to file
                self.data_layer.write_employee_to_file(all_employees)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the employee with the given ID doesn't exist
                tk.messagebox.showinfo("Employee Not Found", f"The employee with ID '{employee_id}' does not exist")

        except Exception as e:
            print("An error occurred:", e)

    def modify_employee(self):  # define a function to modify employee details
        try:
            # Retrieve modified employee details from entry fields
            employee_id = int(self.id_entry.get())
            name = str(self.name_entry.get())
            department = str(self.department_entry.get())
            job_title = str(self.jobTitle_entry.get())
            basic_salary = float(self.basicSalary_entry.get())
            age = int(self.age_entry.get())
            date_of_birth = str(self.dateOfBirth_entry.get())
            passport_details = str(self.passportDetails_entry.get())
            employee_type = EmployeeType(self.employeeType_entry.get())
            # create an Employee object
            employee = Employee(employee_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, employee_type)

            # Retrieve existing employees from data layer
            all_employees = self.data_layer.read_all_employee()

            # Check if employee ID exists
            if employee_id in all_employees:
                # Update employee details
                all_employees[employee_id] = employee
                # Display a message box informing the user that the employee details was modified successfully
                tk.messagebox.showinfo("Employee Modified", f"The employee with ID '{employee_id}' has been modified successfully")
                # Write updated data to file
                self.data_layer.write_employee_to_filee(all_employees)
                # Clear entry boxes
                self.clearBoxes()
            else:
                # Display a message box informing the user that the employee with the given ID doesn't exist
                tk.messagebox.showinfo("Employee Not Found", f"The employee with ID '{employee_id}' does not exist")

        except Exception as e:
            print("An error occurred:", e)


    def display_employee_details(self):  # define a function to display employee details in a table format by calling the ListEmployeeForm
        # display the added employee into the table created in the ListEmployeeForm class
        ListEmployeeForm(dt)

class ListEmployeeForm:
    """Class to represent a GUI form to display data"""

    def __init__(self, data_layer):
        self.data_layer = data_layer  # initialize data layer
        self.root = tk.Tk()  # create a Tkinter root window
        self.root.geometry('1200x400')  # set window size
        self.root.title("Employee Details")  # set window title

        # Create the table to display all employee details
        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Department', 'Job Title', 'Basic Salary', 'Age', 'Date of Birth', 'Passport Details', 'Employee Type'), show='headings')
        # Set column heading for each attribute of the employee
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Department', text='Department')
        self.table.heading('Job Title', text='Job Title')
        self.table.heading('Basic Salary', text='Basic Salary')
        self.table.heading('Age', text='Age')
        self.table.heading('Date of Birth', text='Date of Birth')
        self.table.heading('Passport Details', text='Passport Details')
        self.table.heading('Employee Type', text='Employee Type')
        # Pack the table widget with some padding
        self.table.pack(pady=20)

        # Populate the table with data from the data layer
        all_employees = self.data_layer.read_all_employee()
        for employee_id, employee in all_employees.items():
            # Insert employee data into the table
            self.table.insert('', 'end', values=(employee_id, employee.get_name(), employee.get_department(), employee.get_jobTitle(), employee.get_basicSalary(), employee.get_age(), employee.get_dateOfBirth(), employee.get_passportDetails(), employee.get_employeeType().value))

        self.root.mainloop()

class Employee: # create a class for an employee
    def __init__(self, id, name, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails, employeeType): # define a constructor method to initialize the attributes of the Event class
        self.__id = id
        self.__name = name
        self.__department = department
        self.__jobTitle = jobTitle
        self.__basicSalary = basicSalary
        self.__age = age
        self.__dateOfBirth = dateOfBirth
        self.__passportDetails = passportDetails
        self.__employeeType = employeeType

    def set_id(self, id): # setter method for updating the id
        self.__id = id

    def set_name(self, name): # setter method for updating the name
        self.__name = name

    def set_department(self, department): # setter method for updating the department
        self.__department = department

    def set_jobTitle(self, jobTitle): # setter method for updating the job title
        self.__jobTitle = jobTitle

    def set_basicSalary(self, basicSalary): # setter method for updating the basic salary
        self.__basicSalary = basicSalary

    def set_age(self, age): # setter method for updating the age
        self.__age = age

    def set_dateOfBirth(self, dateOfBirth): # setter method for updating the date of birth
        self.__dateOfBirth = dateOfBirth

    def set_passportDetails(self, passportDetails): # setter method for updating the passport details
        self.__passportDetails = passportDetails

    def set_employeeType(self, employeeType): # setter method for updating the employee type
        self.__employeeType = employeeType

    def get_id(self): # getter method for receiving the id
        return self.__id

    def get_name(self): # getter method for receiving the name
        return self.__name

    def get_department(self): # getter method for receiving the department
        return self.__department

    def get_jobTitle(self): # getter method for receiving the job title
        return self.__jobTitle

    def get_basicSalary(self): # getter method for receiving the basic salary
        return self.__basicSalary

    def get_age(self): # getter method for receiving the age
        return self.__age

    def get_dateOfBirth(self): # getter method for receiving the date of birth
        return self.__dateOfBirth

    def get_passportDetails(self): # getter method for receiving the passport details
        return self.__passportDetails

    def get_employeeType(self): # getter method for receiving the employee type
        return self.__employeeType

    def calculate_salary(self): # define a function for calculating the salary of an employee
        try:
            # Attempt to convert basic_salary to float and return it
            return float(self.__basicSalary)
        except ValueError:
            # If basic salary is not a valid numerical value, raise an exception
            raise ValueError("Basic salary must be a numerical value")

    def __str__(self): # define a function to display information about the employee
        return f"ID: {self.__id}, Name: {self.__name}, Department: {self.__department}, Job Title: {self.__jobTitle}, Basic Salary: {self.__basicSalary}, Age: {self.__age}, Date of Birth: {self.__dateOfBirth}, Passport Details: {self.__passportDetails}, Employee Type: {self.__employeeType.value}"


class DataLayer:
    """Class to handle read and write operations for employee data"""

    def __init__(self, filename):
        self.filename = filename  # store the filename as an instance variable

    def read_all_employee(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.filename):
                # If the file doesn't exist, return an empty dictionary
                return {}
            else:
                # Now open the file in read mode ('rb')
                with open(self.filename, 'rb') as file:
                    # Load the data from the file
                    all_employees = pickle.load(file)
                    return all_employees
        except Exception as e:
            print("An error occurred while reading client data:", e)
            return {}  # Return an empty dictionary if an error occurs

    def write_employee_to_file(self, all_employees):
        try:
            # Open the file in write binary mode ('wb')
            with open(self.filename, 'wb') as f:
                # Write the employee data to the file
                pickle.dump(all_employees, f)
                print("Employee data written to file successfully.")
        except Exception as e:
            print("An error occurred while writing employee data to file:", e)


# Create an instance of the DataLayer class
filename = "employee.pkl"
dt = DataLayer(filename)
# Create an instance of the EmployeeGUI class and pass the data_layer argument
employee_gui = EmployeeGUI(dt)
# Read all employees from the data layer
all_employee = dt.read_all_employee()
# Create an instance of the ListEmployeeForm class to display employee details
show_employee= ListEmployeeForm(dt)