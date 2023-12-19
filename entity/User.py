from util.DBConnUtil import DBConnection


class User(DBConnection):
    def __init__(self):
        super().__init__()
        self.userID = 0
        self.userName = ''
        self.email = ''
        self.password = ''
        self.contactNumber = 0
        self.address = ''

    # SETTERS
    def set_userID(self, value):
        self.userID = value

    def set_userName(self, value):
        self.userName = value

    def set_email(self, value):
        self.email = value

    def set_password(self, value):
        self.password = value

    def set_contactNumber(self, value):
        self.contactNumber = value

    def set_address(self, value):
        self.address = value

    # GETTERS
    def get_userID(self):
        return self.userID

    def get_userName(self):
        return self.userName

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_contactNumber(self):
        return self.contactNumber

    def get_address(self):
        return self.address

    def __str__(self):
        return f'User ID: {self.userID} User Name: {self.userName}\n' \
               f'Email: {self.email} Contact Number: {self.contactNumber} Address: {self.address}'
