from entity.Courier import Courier
from entity.Employee import Employee
from entity.Location import Location


class CourierCompany(Courier, Employee, Location):
    def __init__(self):
        super().__init__()
        self.companyName = ''
        self.courierID = 0
        self.employeeID = 0
        self.locationID = 0

    # SETTERS
    def set_companyName(self, value):
        self.companyName = value

    def set_courierID(self, value):
        self.courierID = value

    def set_employeeID(self, value):
        self.employeeID = value

    def set_locationID(self, value):
        self.locationID = value

    # GETTERS
    def get_companyName(self):
        return self.companyName

    def get_courierID(self):
        return self.courierID

    def get_employeeID(self):
        return self.employeeID

    def get_locationID(self):
        return self.locationID

    def __str__(self):
        return f'Company Name: {self.companyName} Courier ID: {self.courierID}\n' \
               f'Employee ID: {self.employeeID} Location ID: {self.locationID}'
