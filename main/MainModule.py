from dao.ICourierUserService import ICourierUserService
from dao.UserDAO import UserDAO
from dao.CourierDAO import CourierDAO
from dao.EmployeeDAO import EmployeeDAO
from dao.LocationDAO import LocationDAO
from dao.CourierCompanyDAO import CourierCompanyDAO
from dao.PaymentDAO import PaymentDAO
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
from exception.InvalidEmployeeIdException import InvalidEmployeeIdException
from util.DBConnUtil import DBConnection


def main():

    dbconnection = DBConnection()

    try:
        dbconnection.open()
        print("--Database Is Connected:--")
    except Exception as e:
        print(e)

    try:
        print("=" * 30)
        print("Courier Management System")
        print("=" * 30)
        print("Welcome to Courier Management System!")

        courier_management_system = ICourierUserService()

        while True:
            print("1.User 2.Courier 3.Employee 4.Location 5.CourierCompany 6.Payment 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                u = UserDAO()
                u.perform_user_actions()
            elif ch == 2:
                c = CourierDAO()
                c.perform_courier_actions()
            elif ch == 3:
                e = EmployeeDAO()
                e.perform_employee_actions()
            elif ch == 4:
                l = LocationDAO()
                l.perform_location_actions()
            elif ch == 5:
                cc = CourierCompanyDAO()
                cc.perform_courier_company_actions()
            elif ch == 6:
                p = PaymentDAO()
                p.perform_payment_actions()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

        while True:
            print("=" * 10)
            print("---MENU---")
            print("=" * 10)
            print("1.placeOrder\n2.getOrderStatus\n3.cancelOrder\n4.getAssignedOrder\n0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(f'Tracking Number of newly placed Order is {courier_management_system.placeOrder()}')
            elif ch == 2:
                print(courier_management_system.getOrderStatus(int(input('Enter Tracking Number of the Courier to get Order Status: '))))
            elif ch == 3:
                print(courier_management_system.cancelOrder(int(input('Enter Tracking Number of the Courier to be Cancelled: '))))
            elif ch == 4:
                print(courier_management_system.getAssignedOrder(int(input('Enter Employee ID to list the courier orders assigned to him/her: '))))
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    except TrackingNumberNotFoundException as e:
        print(e)

    except InvalidEmployeeIdException as e:
        print(e)

    except Exception as e:
        print(e)

    finally:
        dbconnection.close()
        print("Thankyou for visiting Courier Management System!")
        print("--Connection Is Closed:--")


if __name__ == "__main__":
    main()
