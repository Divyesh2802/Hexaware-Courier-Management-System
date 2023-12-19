class InvalidEmployeeIdException(Exception):
    def __init__(self, employee_id):
        super().__init__(f"Invalid Employee ID: {employee_id}. Employee not found in the system.")
