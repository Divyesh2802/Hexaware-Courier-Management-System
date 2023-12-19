from entity.Employee import Employee


class EmployeeDAO(Employee):
    def __init__(self):
        super().__init__()

    def perform_employee_actions(self):
        while True:
            print("(Employee) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_employee_table()
            elif ch == 2:
                print(self.add_employee())
            elif ch == 3:
                print(self.update_employee())
            elif ch == 4:
                print(self.delete_employee())
            elif ch == 5:
                self.select_employee()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_employee_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Employee (
            employeeID INT PRIMARY KEY,
            employeeName VARCHAR(50),
            email VARCHAR(50),
            contactNumber INT,
            role VARCHAR(50),
            salary FLOAT)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Employee Table Created successfully.')
        except Exception as e:
            print(e)

    def add_employee(self):
        try:
            self.open()
            self.employeeID = int(input('Enter Employee ID: '))
            self.employeeName = input('Enter Employee Name: ')
            self.email = input('Enter email: ')
            self.contactNumber = int(input('Enter contact number: '))
            self.role = input('Enter role: ')
            self.salary = float(input('Enter salary: '))
            data = [(self.employeeID, self.employeeName, self.email, self.contactNumber, self.role, self.salary)]
            insert_str = '''INSERT INTO Employee(employeeID, employeeName, email, contactNumber, role, salary) 
                            VALUES(%s, %s, %s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_employee(self):
        try:
            self.open()
            employee_id = int(input('Input Employee ID to be Updated: '))
            self.employeeName = input('Enter Employee Name: ')
            self.email = input('Enter email: ')
            self.contactNumber = int(input('Enter contact number: '))
            self.role = input('Enter role: ')
            self.salary = float(input('Enter salary: '))
            data = [(self.employeeName, self.email, self.contactNumber, self.role, self.salary, employee_id)]
            update_str = '''UPDATE Employee SET employeeName=%s, email=%s, contactNumber=%s, role=%s, salary=%s
                            WHERE employeeID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_employee(self):
        try:
            self.open()
            employee_id = int(input('Input Employee ID to be Deleted: '))
            delete_str = f'''DELETE FROM Employee WHERE employeeID = {employee_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_employee(self):
        try:
            select_str = '''SELECT * FROM Employee'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Employee Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)
