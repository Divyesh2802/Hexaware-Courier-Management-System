from dao.CourierDAO import CourierDAO
from dao.CourierCompanyDAO import CourierCompanyDAO
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
from exception.InvalidEmployeeIdException import InvalidEmployeeIdException


class ICourierUserService(CourierCompanyDAO, CourierDAO):
    def __init__(self):
        super().__init__()

    # PLACE ORDER
    def placeOrder(self):
        print('Enter Courier Details to Place a new courier order: ')
        print(self.add_courier())
        try:
            self.open()
            self.stmt.execute(f'''SELECT trackingNumber FROM Courier WHERE courierID = {self.courierID}''')
            records = self.stmt.fetchone()[0]
            self.close()
            return records
        except Exception as e:
            return e

    # GET ORDER STATUS
    def getOrderStatus(self, trackingNumber):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM Courier WHERE trackingNumber = {trackingNumber}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise TrackingNumberNotFoundException(trackingNumber)
            else:
                self.stmt.execute(f'''SELECT status FROM Courier WHERE trackingNumber = {trackingNumber}''')
                records = self.stmt.fetchone()[0]
                self.close()
                return records
        except TrackingNumberNotFoundException as e:
            return e
        except Exception as e:
            return e

    # CANCEL ORDER
    def cancelOrder(self, trackingNumber):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM Courier WHERE trackingNumber = {trackingNumber}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise TrackingNumberNotFoundException(trackingNumber)
            else:
                self.stmt.execute(f'''UPDATE Courier SET status = "Cancelled" WHERE trackingNumber = {trackingNumber}''')
                self.conn.commit()
                self.close()
                return True
        except TrackingNumberNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False

    # GET ASSIGNED ORDER
    def getAssignedOrder(self, employeeID):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM Employee WHERE employeeID = {employeeID}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise InvalidEmployeeIdException(employeeID)
            else:
                self.stmt.execute(f'''SELECT * FROM Courier AS C JOIN CourierCompany AS CC ON C.courierID = CC.courierID
                                    WHERE CC.employeeID = {employeeID}''')
                records = self.stmt.fetchall()
                self.close()
                return records
        except InvalidEmployeeIdException as e:
            return e
        except Exception as e:
            return e
