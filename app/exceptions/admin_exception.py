

class EmptyAdminTableException(Exception):
    def __init__(self, msg: str = "Admin Table is empty"):
        self.msg = msg
        super().__init__(self.msg)




class AdminDoesNotExistException(Exception):
    def __init__(self, msg: str = "Admin is not available"):
        self.msg = msg
        super().__init__(self.msg)
