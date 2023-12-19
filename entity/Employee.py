from util.DBConnUtil import DBConnection


class Employee(DBConnection):
    def __init__(self):
        super().__init__()
        self.employeeID = 0
        self.employeeName = ''
        self.email = ''
        self.contactNumber = 0
        self.role = ''
        self.salary = 0.0

    # SETTERS
    def set_employeeID(self, value):
        self.employeeID = value

    def set_employeeName(self, value):
        self.employeeName = value

    def set_email(self, value):
        self.email = value

    def set_contactNumber(self, value):
        self.contactNumber = value

    def set_role(self, value):
        self.role = value

    def set_salary(self, value):
        self.salary = value

    # GETTERS
    def get_employeeID(self):
        return self.employeeID

    def get_employeeName(self):
        return self.employeeName

    def get_email(self):
        return self.email

    def get_contactNumber(self):
        return self.contactNumber

    def get_role(self):
        return self.role

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f'Employee ID: {self.employeeID} Name: {self.employeeName}\n' \
               f'Email: {self.email} Contact Number: {self.contactNumber}\n' \
               f'Role: {self.role} Salary: {self.salary}'
