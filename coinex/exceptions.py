class CoinExBaseException(Exception):
    default_message = ""
    default_code = 0

    def __init__(self, message="", code=0):
        self.message = self.default_message if not message else message
        self.code = self.default_code if not code else code

    def __str__(self):
        return self.message


class RequestFailedToSendException(CoinExBaseException):
    default_message = "Request to server failed"
    default_code = 1
