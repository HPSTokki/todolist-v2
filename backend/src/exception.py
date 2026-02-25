from fastapi import status

class DomainException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__()
        
class TaskNotFound(DomainException):
    def __init__(self, message):
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND
        )