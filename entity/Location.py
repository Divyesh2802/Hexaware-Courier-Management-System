from util.DBConnUtil import DBConnection


class Location(DBConnection):
    def __init__(self):
        super().__init__()
        self.locationID = 0
        self.locationName = ''
        self.address = ''

    # SETTERS
    def set_locationID(self, value):
        self.locationID = value

    def set_locationName(self, value):
        self.locationName = value

    def set_address(self, value):
        self.address = value

    # GETTERS
    def get_locationID(self):
        return self.locationID

    def get_locationName(self):
        return self.locationName

    def get_address(self):
        return self.address

    def __str__(self):
        return f'Location ID: {self.locationID} Name: {self.locationName}\n' \
               f'Address: {self.address}'
