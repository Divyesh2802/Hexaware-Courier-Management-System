from entity.Location import Location


class LocationDAO(Location):
    def __init__(self):
        super().__init__()

    def perform_location_actions(self):
        while True:
            print("(Location) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_location_table()
            elif ch == 2:
                print(self.add_location())
            elif ch == 3:
                print(self.update_location())
            elif ch == 4:
                print(self.delete_location())
            elif ch == 5:
                self.select_location()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_location_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Location (
            locationID INT PRIMARY KEY,
            locationName VARCHAR(50),
            address VARCHAR(50))'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Location Table Created successfully.')
        except Exception as e:
            print(e)

    def add_location(self):
        try:
            self.open()
            self.locationID = int(input('Enter Location ID: '))
            self.locationName = input('Enter Location Name: ')
            self.address = input('Enter address: ')
            data = [(self.locationID, self.locationName, self.address)]
            insert_str = '''INSERT INTO Location(locationID, locationName, address) 
                            VALUES(%s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_location(self):
        try:
            self.open()
            location_id = int(input('Input Location ID to be Updated: '))
            self.locationName = input('Enter Location Name: ')
            self.address = input('Enter address: ')
            data = [(self.locationName, self.address, location_id)]
            update_str = '''UPDATE Location SET locationName=%s, address=%s
                            WHERE locationID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_location(self):
        try:
            self.open()
            location_id = int(input('Input Location ID to be Deleted: '))
            delete_str = f'''DELETE FROM Location WHERE locationID = {location_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_location(self):
        try:
            select_str = '''SELECT * FROM Location'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Location Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)
