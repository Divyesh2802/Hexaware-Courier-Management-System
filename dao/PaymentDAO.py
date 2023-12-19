from entity.Payment import Payment


class PaymentDAO(Payment):
    def __init__(self):
        super().__init__()

    def perform_payment_actions(self):
        while True:
            print("(Payment) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_payment_table()
            elif ch == 2:
                print(self.add_payment())
            elif ch == 3:
                print(self.update_payment())
            elif ch == 4:
                print(self.delete_payment())
            elif ch == 5:
                self.select_payment()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_payment_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Payment (
            paymentID INT PRIMARY KEY,
            courierID INT,
            amount FLOAT,
            paymentDate DATE,
            FOREIGN KEY(courierID) REFERENCES Courier(courierID) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Payment Table Created successfully.')
        except Exception as e:
            print(e)

    def add_payment(self):
        try:
            self.open()
            self.paymentID = int(input('Enter Payment ID: '))
            self.courierID = int(input('Enter Courier ID: '))
            self.amount = float(input('Enter Amount: '))
            self.paymentDate = input('Enter Payment Date: ')
            data = [(self.paymentID, self.courierID, self.amount, self.paymentDate)]
            insert_str = '''INSERT INTO Payment(paymentID, courierID, amount, paymentDate) 
                            VALUES(%s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_payment(self):
        try:
            self.open()
            payment_id = int(input('Input Payment ID to be Updated: '))
            self.courierID = int(input('Enter Courier ID: '))
            self.amount = float(input('Enter Amount: '))
            self.paymentDate = input('Enter Payment Date: ')
            data = [(self.courierID, self.amount, self.paymentDate, payment_id)]
            update_str = '''UPDATE Payment SET courierID=%s, amount=%s, paymentDate=%s
                            WHERE paymentID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_payment(self):
        try:
            self.open()
            payment_id = int(input('Input Payment ID to be Deleted: '))
            delete_str = f'''DELETE FROM Payment WHERE paymentID = {payment_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_payment(self):
        try:
            select_str = '''SELECT * FROM Payment'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Payment Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)
