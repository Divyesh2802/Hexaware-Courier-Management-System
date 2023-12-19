from entity.CourierCompany import CourierCompany


class CourierCompanyDAO(CourierCompany):
    def __init__(self):
        super().__init__()

    def perform_courier_company_actions(self):
        while True:
            print("(CourierCompany) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_courier_company_table()
            elif ch == 2:
                print(self.add_courier_company())
            elif ch == 3:
                print(self.update_courier_company())
            elif ch == 4:
                print(self.delete_courier_company())
            elif ch == 5:
                self.select_courier_company()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_courier_company_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS CourierCompany (
            companyName VARCHAR(50) PRIMARY KEY,
            courierID INT,
            employeeID INT,
            locationID INT,
            FOREIGN KEY(courierID) REFERENCES Courier(courierID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(locationID) REFERENCES Location(locationID) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('CourierCompany Table Created successfully.')
        except Exception as e:
            print(e)

    def add_courier_company(self):
        try:
            self.open()
            self.companyName = input('Enter Company Name: ')
            self.courierID = int(input('Enter Courier ID: '))
            self.employeeID = int(input('Enter Employee ID: '))
            self.locationID = int(input('Enter Location ID: '))
            data = [(self.companyName, self.courierID, self.employeeID, self.locationID)]
            insert_str = '''INSERT INTO CourierCompany(companyName, courierID, employeeID, locationID) 
                            VALUES(%s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_courier_company(self):
        try:
            self.open()
            company_name = input('Enter Company Name to be Updated: ')
            self.courierID = int(input('Enter Courier ID: '))
            self.employeeID = int(input('Enter Employee ID: '))
            self.locationID = int(input('Enter Location ID: '))
            data = [(self.courierID, self.employeeID, self.locationID, company_name)]
            update_str = '''UPDATE CourierCompany SET courierID=%s, employeeID=%s, locationID=%s
                            WHERE companyName = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_courier_company(self):
        try:
            self.open()
            company_name = input('Enter Company Name to be Deleted: ')
            delete_str = f'''DELETE FROM CourierCompany WHERE companyName = '{company_name}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_courier_company(self):
        try:
            select_str = '''SELECT * FROM CourierCompany'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In CourierCompany Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)

    def getAssignedOrder(self, employeeID):
        pass
