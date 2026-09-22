class InvalidDepartmentEmailException(Exception):
    def __init__(self, msg : str = "Invalid Email Address"):
        self.msg = msg
        super().__init__(self.msg)