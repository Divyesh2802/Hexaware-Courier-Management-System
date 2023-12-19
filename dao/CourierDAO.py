from entity.Courier import Courier


class CourierDAO(Courier):
    def __init__(self):
        super().__init__()

    def perform_courier_actions(self):
        while True:
            print("(Courier) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_courier_table()
            elif ch == 2:
                print(self.add_courier())
            elif ch == 3:
                print(self.update_courier())
            elif ch == 4:
                print(self.delete_courier())
            elif ch == 5:
                self.select_courier()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_courier_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Courier (
            courierID INT PRIMARY KEY,
            senderName VARCHAR(50),
            senderAddress VARCHAR(50),
            receiverName VARCHAR(50),
            receiverAddress VARCHAR(50),
            weight FLOAT,
            status VARCHAR(50),
            trackingNumber INT,
            deliveryDate DATE,
            userID INT,
            FOREIGN KEY(userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Courier Table Created successfully.')
        except Exception as e:
            print(e)

    def add_courier(self):
        try:
            self.open()
            self.courierID = int(input('Enter Courier ID: '))
            self.senderName = input('Enter Sender Name: ')
            self.senderAddress = input('Enter Sender Address: ')
            self.receiverName = input('Enter Receiver Name: ')
            self.receiverAddress = input('Enter Receiver Address: ')
            self.weight = float(input('Enter Weight: '))
            self.status = input('Enter Status: ')
            self.trackingNumber = int(input('Enter Tracking Number: '))
            self.deliveryDate = input('Enter Delivery Date: ')
            self.userID = int(input('Enter User ID: '))
            data = [(self.courierID, self.senderName, self.senderAddress, self.receiverName, self.receiverAddress,
                     self.weight, self.status, self.trackingNumber, self.deliveryDate, self.userID)]
            insert_str = '''INSERT INTO Courier(courierID, senderName, senderAddress, receiverName, receiverAddress,
                            weight, status, trackingNumber, deliveryDate, userID) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_courier(self):
        try:
            self.open()
            courier_id = int(input('Input Courier ID to be Updated: '))
            self.senderName = input('Enter Sender Name: ')
            self.senderAddress = input('Enter Sender Address: ')
            self.receiverName = input('Enter Receiver Name: ')
            self.receiverAddress = input('Enter Receiver Address: ')
            self.weight = float(input('Enter Weight: '))
            self.status = input('Enter Status: ')
            self.trackingNumber = int(input('Enter Tracking Number: '))
            self.deliveryDate = input('Enter Delivery Date: ')
            self.userID = int(input('Enter User ID: '))
            data = [(self.senderName, self.senderAddress, self.receiverName, self.receiverAddress,
                     self.weight, self.status, self.trackingNumber, self.deliveryDate, self.userID, courier_id)]
            update_str = '''UPDATE Courier SET senderName=%s, senderAddress=%s, receiverName=%s, receiverAddress=%s,
                            weight=%s, status=%s, trackingNumber=%s, deliveryDate=%s, userID=%s
                            WHERE courierID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_courier(self):
        try:
            self.open()
            courier_id = int(input('Input Courier ID to be Deleted: '))
            delete_str = f'''DELETE FROM Courier WHERE courierID = {courier_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_courier(self):
        try:
            select_str = '''SELECT * FROM Courier'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Courier Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)

    def placeOrder(self):
        pass

    def getOrderStatus(self, trackingNumber):
        pass

    def cancelOrder(self, trackingNumber):
        pass
