from entity.Courier import Courier


class Payment(Courier):
    def __init__(self):
        super().__init__()
        self.paymentID = 0
        self.courierID = 0
        self.amount = 0.0
        self.paymentDate = ''

    # SETTERS
    def set_paymentID(self, value):
        self.paymentID = value

    def set_courierID(self, value):
        self.courierID = value

    def set_amount(self, value):
        self.amount = value

    def set_paymentDate(self, value):
        self.paymentDate = value

    # GETTERS
    def get_paymentID(self):
        return self.paymentID

    def get_courierID(self):
        return self.courierID

    def get_amount(self):
        return self.amount

    def get_paymentDate(self):
        return self.paymentDate

    def __str__(self):
        return f'Payment ID: {self.paymentID} Courier ID: {self.courierID}\n' \
               f'Amount: {self.amount} Payment Date: {self.paymentDate}'
