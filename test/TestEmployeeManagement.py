import unittest
from dao.EmployeeDAO import EmployeeDAO


class MyTestCase(unittest.TestCase):
    # SET UP
    def setUp(self):
        print("Set Up")
        self.obj1 = EmployeeDAO()

    # TEST EMPLOYEE IS ADDED OR NOT
    def test_add_employee(self):
        print("test_add_employee")
        result = self.obj1.add_employee()
        self.assertEqual(result, True)

    def test_add_employee_exception(self):
        print("test_add_employee_exception")
        result = self.obj1.add_employee()
        self.assertRaises(Exception, result)

    # TEAR DOWN
    def tearDown(self):
        print("Tear Down")


if __name__ == '__main__':
    unittest.main()
