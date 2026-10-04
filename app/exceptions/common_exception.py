class InvalidEmailException(Exception):
    def __init__(self, msg : str = "Invalid Email Address"):
        self.msg = msg
        super().__init__(self.msg)


class InvalidIdException(Exception):
    def __init__(self, name, id):
        self.msg = f"Invalid {name} ID : {id}"
        super().__init__(self.msg)


class EmailAlreadyRegisteredException(Exception):
    def __init__(self, email):
        self.msg = f"Email: {email} is already registered."
        super().__init__(self.msg)


class EmptyTableException(Exception):
    def __init__(self, name):
        self.msg = f"Currently {name} details are not available."
        super().__init__(self.msg)