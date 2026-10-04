# class InvalidADminEmailException(Exception):
#     def __init__(self, msg : str = "Invalid Admin Email Address"):
#         self.msg = msg
#         super().__init__(self.msg)

class EmptyAdminTableException(Exception):
    def __init__(self, msg: str = "Admin Table is empty"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidAdminIdException(Exception):
    def __init__(self, msg: str = "Provided Admin ID is invalid"):
        self.msg = msg
        super().__init__(self.msg)


class AdminDoesNotExistException(Exception):
    def __init__(self, msg: str = "Admin is not available"):
        self.msg = msg
        super().__init__(self.msg)
