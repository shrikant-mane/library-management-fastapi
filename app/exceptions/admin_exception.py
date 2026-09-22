class InvalidADminEmailException(Exception):
    def __init__(self, msg : str = "Invalid Admin Email Address"):
        self.msg = msg
        super().__init__(self.msg)