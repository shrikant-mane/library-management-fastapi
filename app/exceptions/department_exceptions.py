
class EmptyDepartmentTableException(Exception):
    def __init__(self, msg: str = "Currently departments details are not availabe"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidDepartmentIdException(Exception):
    def __init__(self, _department_id):
        self.msg = f"Department ID : {_department_id} is not available."
        super().__init__(self.msg)

class InvalidDepartmentNameException(Exception):
    def __init__(self, _department_name):
        self.msg = f"Department Name : {_department_name} is not available."
        super().__init__(self.msg)