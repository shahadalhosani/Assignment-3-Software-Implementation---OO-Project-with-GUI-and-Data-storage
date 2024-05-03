from enum import Enum

class EmployeeType(Enum):
    Manager = "Sales Manager"
    Sales_Person = "Sales person"
    Marketing_Manager = "Marketing Manager"
    Marketer = "Marketer"
    Accountant = "Accountant"
    Designer = "Designer"
    Handyman = "Handyman"

class Entity: # create a parent class that the child classes would inherit attributes and functions from
    def __init__(self, id, name, address, contactDetails): # define a constructor method to initialize the attributes of the Entity class
        self.__id = id
        self.__name = name
        self.__address = address
        self.__contactDetails = contactDetails

    def set_id(self, id):  # setter method for updating the id
        self.__id = id

    def set_name(self, name):  # setter method for updating the name
        self.__name = name

    def set_address(self, address):  # setter method for updating the address
        self.__address = address

    def set_contactDetails(self, contactDetails):  # setter method for updating the contactDetails
        self.__contactDetails = contactDetails

    def get_id(self):  # getter method for receiving the id
        return self.__id

    def get_name(self):  # getter method for receiving the name
        return self.__name

    def get_address(self):  # getter method for receiving the address
        return self.__address

    def get_contactDetails(self):  # getter method for receiving the contactDetails
       return self.__contactDetails

    def __str__(self): # define a function to display information about the Entity
        return f"ID: {self.__id}, Name: {self.__name}, Address: {self.__address}, Contact Details: {self.__contactDetails}"

class Client(Entity): # create a class for the client, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails, budget):  # define a constructor method to initialize the attributes of the Client class
        super().__init__(id, name, address, contactDetails)  # call the attributes of the parent class
        self.__budget = budget
        self.__events = []  # create a list to store events associated with a client

    def set_budget(self, budget):  # setter method for updating the budget
        self.__budget = budget

    def get_budget(self):  # getter method for receiving the budget
        return self.__budget

    # implement a composition relationship between client and event
    def add_event(self, eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        self.__events.append(Event(eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice))  # add an event to the list

    def get_event(self):  # getter method for receiving the event that a client has
        total_events=""
        for event in self.__events:
            total_events=str(event)
        return total_events

    def __str__(self):  # define a function to display information about the Client
        return super().__str__() + f", Client Budget: {self.__budget}\nEvents to organize: {self.get_event()}"

class Guest(Entity): # create a class for the guest, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails, status): # define a constructor method to initialize the attributes of the Client class
        super().__init__(id, name, address, contactDetails)  # call the attributes of the parent class
        self.__status = status

    def set_status(self, status):  # setter method for updating the status
        self.__status = status

    def get_status(self):  # getter method for receiving the status
        return self.__status

    def __str__(self):  # define a function to display information about the Guest
        return super().__str__() + f", Guest Status: {self.__status}"

class Supplier(Entity): # create a class for the supplier, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails): # define a constructor method to initialize the attributes of the Supplier class
        super().__init__(id, name, address, contactDetails)  # call the attributes of the parent class

    def __str__(self):  # define a function to display information about the Supplier
        return super().__str__()

class Venue(Entity): # create a class for the venue, which inherits attributes and function from the Entity class
    def __init__(self, id, name, address, contactDetails, maxGuests, minGuests):  # define a constructor method to initialize the attributes of the Venue class
        super().__init__(id, name, address, contactDetails)  # call the attributes of the parent class
        self.__maxGuests = maxGuests
        self.__minGuests = minGuests
        self.__events = []  # create a list to store events associated with a venue

    def set_maxGuests(self, maxGuests):  # setter method for updating the maximum number of guests
        self.__maxGuests = maxGuests

    def set_minGuests(self, minGuests):  # setter method for updating the minimum number of guests
        self.__minGuests = minGuests

    def get_maxGuests(self):  # getter method for receiving the maximum number of guests
        return self.__maxGuests

    def get_minGuests(self):  # getter method for receiving the minimum number of guests
        return self.__minGuests

    # implement a composition relationship between venue and event
    def add_event(self, eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        self.__events.append(Event(eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, venueAddress, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice))  # add event to the list

    def get_event(self):  # getter method for receiving the event that a venue has
        total_events=""
        for event in self.__events:
            total_events=str(event)
        return total_events

    def __str__(self):  # define a function to display information about the Supplier
        return super().__str__() + f", Venue Maximum Guests: {self.__maxGuests}, Venue Minimum Guests: {self.__minGuests}\nEvent Hosted: {self.get_event()}"

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
        self.__employees = []  # create a list to store employees associated with a specific event
        self.__guest = []  # create a list to store guests associated with a specific event
        self.__supplier = []  # create a list to store suppliers associated with a specific event
        self.__caterer = []  # create a list to store caterers associated with a specific event

    def set_eventID(self, eventID):  # setter method for updating the event id
        self.__eventID = eventID

    def set_eventType(self, eventType):  # setter method for updating the event type
        self.__eventType = eventType

    def set_eventTheme(self, eventTheme):  # setter method for updating the event theme
        self.__eventTheme = eventTheme

    def set_eventDate(self, eventDate):  # setter method for updating the event date
        self.__eventDate = eventDate

    def set_eventTime(self, eventTime):  # setter method for updating the event time
        self.__eventTime = eventTime

    def set_eventDuration(self, eventDuration):  # setter method for updating the event duration
        self.__eventDuration = eventDuration

    def set_venueAddress(self, venueAddress):  # setter method for updating the catering company
        self.__venueAddress = venueAddress

    def set_cateringCompany(self, cateringCompany):  # setter method for updating the maximum number of guests
        self.__cateringCompany = cateringCompany

    def set_cleaningCompany(self, cleaningCompany):  # setter method for updating the cleaning company
        self.__cleaningCompany = cleaningCompany

    def set_decorationsCompany(self, decorationsCompany):  # setter method for updating the decorations company
        self.__decorationsCompany = decorationsCompany

    def set_entertainmentCompany(self, entertainmentCompany):  # setter method for updating the entertainment company
        self.__entertainmentCompany = entertainmentCompany

    def set_furnitureSupplyCompany(self, furnitureSupplyCompany):  # setter method for updating the furniture supply company
        self.__furnitureSupplyCompany = furnitureSupplyCompany

    def set_invoice(self, invoice):  # setter method for updating the invoice
        self.__invoice = invoice

    def get_eventID(self):  # getter method for receiving the event id
        return self.__eventID

    def get_eventType(self):  # getter method for receiving the event type
        return self.__eventType

    def get_eventTheme(self):  # getter method for receiving the event theme
        return self.__eventTheme

    def get_eventDate(self):  # getter method for receiving the event date
        return self.__eventDate

    def get_eventTime(self):  # getter method for receiving the event time
        return self.__eventTime

    def get_eventDuration(self):  # getter method for receiving the event duration
        return self.__eventDuration

    def get_venueAddress(self):  # getter method for receiving the venue address
        return self.__venueAddress

    def get_cateringCompany(self):  # getter method for receiving the catering company
        return self.__cateringCompany

    def get_cleaningCompany(self):  # getter method for receiving the cleaning company
        return self.__cleaningCompany

    def get_decorationsCompany(self):  # getter method for receiving the decorations company
        return self.__decorationsCompany

    def get_entertainmentCompany(self):  # getter method for receiving the entertainment company
        return self.__entertainmentCompany

    def get_furnitureSupplyCompany(self):  # getter method for receiving the furniture supply company
        return self.__furnitureSupplyCompany

    def get_invoice(self):  # getter method for receiving the minimum invoice
        return self.__invoice

    # implementing a unary association relationship between event and employees
    def add_employees(self, employees):
        self.__employees.append(employees)  # add employee to the list

    def get_employees(self): #getter method for receiving the employees that an event has
        print(f"The event with ID {self.get_eventID()} employees:")
        for employee in self.__employees:
            print(employee)

    # implementing an aggregation relationship between event and supplier
    def add_supplier(self, supplier):
        self.__supplier.append(supplier)  # add supplier to the list

    def get_suppliers(self):  # getter method for receiving the supplier that an event has
        total_supplier = ""
        for supplier in self.__supplier:
            total_supplier+=str(supplier)
        return total_supplier

    # implementing an aggregation relationship between event and caterer
    def add_caterer(self, caterer):
        self.__caterer.append(caterer)  # add caterer to the list

    def get_caterer(self):  # getter method for receiving the caterer that an event has
        total_caterer = ""
        for caterer in self.__caterer:
            total_caterer+=str(caterer)
        return total_caterer

    # implementing a composition relationship between event and guests
    def add_guests(self, id, name, address, contactDetails, status):
        self.__guest.append(Guest(id, name, address, contactDetails, status))  # add guest to the list

    def get_guests(self):  # getter method for receiving the guest that an event has
        total_guests = ""
        for guest in self.__guest:
            total_guests+=str(guest)
        return total_guests

    def __str__(self):  # define a function to display information about the Event
        return f"ID: {self.__eventID}, Type: {self.__eventType}, Theme: {self.__eventTheme}, Date: {self.__eventDate}, Time: {self.__eventTime}, Duration: {self.__eventDuration}, Venue Address: {self.__venueAddress}, Catering Company: {self.__cateringCompany}, Cleaning Company: {self.__cleaningCompany}, Decorations Company: {self.__decorationsCompany}, Entertainment Company: {self.__entertainmentCompany}, Furniture Supply Company: {self.__furnitureSupplyCompany}, Invoice: {self.__invoice}\nSuppliers: {self.get_suppliers()}\nCaterers: {self.get_caterer()}\nGuests: {self.get_guests()}"


class Employee:  # create a class for an employee
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

    def set_id(self, id):  # setter method for updating the id
        self.__id = id

    def set_name(self, name):  # setter method for updating the name
        self.__name = name

    def set_department(self, department):  # setter method for updating the department
        self.__department = department

    def set_jobTitle(self, jobTitle):  # setter method for updating the job title
        self.__jobTitle = jobTitle

    def set_basicSalary(self, basicSalary):  # setter method for updating the basic salary
        self.__basicSalary = basicSalary

    def set_age(self, age):  # setter method for updating the age
        self.__age = age

    def set_dateOfBirth(self, dateOfBirth):  # setter method for updating the date of birth
        self.__dateOfBirth = dateOfBirth

    def set_passportDetails(self, passportDetails): # setter method for updating the passport details
        self.__passportDetails = passportDetails

    def set_employeeType(self, employeeType):  # setter method for updating the employee type
        self.__employeeType = employeeType

    def get_id(self):  # getter method for receiving the id
        return self.__id

    def get_name(self):  # getter method for receiving the name
        return self.__name

    def get_department(self):  # getter method for receiving the department
        return self.__department

    def get_jobTitle(self):  # getter method for receiving the job title
        return self.__jobTitle

    def get_basicSalary(self):  # getter method for receiving the basic salary
        return self.__basicSalary

    def get_age(self):  # getter method for receiving the age
        return self.__age

    def get_dateOfBirth(self):  # getter method for receiving the date of birth
        return self.__dateOfBirth

    def get_passportDetails(self):  # getter method for receiving the passport details
        return self.__passportDetails

    def get_employeeType(self):  # getter method for receiving the employee type
        return self.__employeeType

    def calculate_salary(self):  # define a function for calculating the salary of an employee
        try:
            # Attempt to convert basic_salary to float and return it
            return float(self.__basicSalary)
        except ValueError:
            # If basic salary is not a valid numerical value, raise an exception
            raise ValueError("Basic salary must be a numerical value")

    def __str__(self):  # define a function to display information about the employee
        return f"ID: {self.__id}, Name: {self.__name}, Department: {self.__department}, Job Title: {self.__jobTitle}, Basic Salary: {self.__basicSalary}, Age: {self.__age}, Date of Birth: {self.__dateOfBirth}, Passport Details: {self.__passportDetails}, Employee Type: {self.__employeeType.value}"

class Manager: # create a class for a manager
    def __init__(self, managerID, managerName):  # define a constructor method to initialize the attributes of the Event class
        self.__managerID = managerID
        self.__managerName = managerName
        self.__employees = []  # create a list to store employees associated with a manager

    def set_managerID(self, manageriD):  # setter method for updating the manager id
        self.__managerID = manageriD

    def set_managerName(self, managerName):  # setter method for updating the manager name
        self.__managerName = managerName

    def get_managerID(self):  # getter method for receiving the manager id
        return self.__managerID

    def get_managerName(self):  # getter method for receiving the manager name
        return self.__managerName

    # implementing an aggregation relationship between Manager and Employees
    def add_employees(self, employee):
        self.__employees.append(employee)  # add employee to the list

    def get_employees(self):  # getter method for receiving the list of employees that are managed by a certain manager
        total_employees=""
        for employee in self.__employees:
            total_employees+=str(employee)
        return total_employees

    def __str__(self):  # define a function to display information about the manager with its associated employees
        return f"Manager ID: {self.__managerID}, Manager Name: {self.__managerName}\nList of Managed Employees:\n{self.get_employees()}"


# Test cases to ensure that the relationships are working

# Example of Inheritance with Entity
guest = Guest(5, "Shahad", "Khalifa city", 505551041, "Regular")
print("Guest Details:")
print(guest)


# All relationships with Event
event1 = Event(1, "Wedding", "Classic", "2024-06-15", 12.00, "4 hours", "Emirates Palace", "Best Catering", "CleanYourSpace", "Appeal Company", None, None, None)
# aggregation between event and caterer
caterer1 = Caterer(1, "Delicious Foods", "123 Oak St", 503847923, 100, 50)
event1.add_caterer(caterer1)
# aggregation between event and supplier
supplier1 = Supplier(1, "Catering Ltd", "789 Elm St", 298874734)
event1.add_supplier(supplier1)
# composition between event and guests
event1.add_guests(1, "Ali", "123 Elm St", 5034979834, "VIP")
event1.add_guests(2, "Fatima", "456 Elm St", 5034739493, "Regular")

print("\nEvent Details:")
print(event1)


# All relationships with Client
client1 = Client(2, "Jane Smith", "456 Oak St", "987-654-3210", 8000)
# composition between client and event
client1.add_event(3, "Birthday", "Princess", "2024-08-10", 12.00, "4 hours", "123 Main St", "Hafla", "Urban", "Decorious", "Walt Disney", "Athoor", None)
print("\nClient Details:")
print(client1)


# All relationships with Venue
venue1 = Venue(4, "Emirates Palace", "Corniche Road", 20345934, 300, 150)
# composition between venue and event
venue1.add_event(5, "Graduation", "Floral", "2024-07-10", 5.00, "5 hours", "Emirates Palace", "All of a Kind Catering", "Smile Handyy", "Decorative Company", "DJ", None, None)
print("\nVenue Details:")
print(venue1)


# All relationships with Manager
manager1 = Manager(1, "Ahmed Ali")
# aggregation between manager and employee
employee2 = Employee("Khaled", 2, "Sales", "Developer", 30000, 25, "1995-05-05", "DEF456", EmployeeType.Sales_Person)
employee3 = Employee("Wafa", 3, "Decor", "Leader", 40000, 27, "1993-07-03", "ABF345", EmployeeType.Manager)
manager1.add_employees(employee2)
manager1.add_employees(employee3)
print("\nManager Details:")
print(manager1)




