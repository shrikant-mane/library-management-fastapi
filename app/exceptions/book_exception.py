class EmptyBookTableException(Exception):
    def __init__(self, msg: str = "Currently book details are not availabe"):
        self.msg = msg
        super().__init__(self.msg)