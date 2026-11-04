class CarmenAPIConfigError(Exception):
    """
    Exception raised when the provided options for TransportAPIClient are invalid.

    Args:
        message (str): The error message.

    Attributes:
        name (str): The name of the exception.
    """
    def __init__(self, message):
        super().__init__(message)
        self.name = "CarmenAPIConfigError"

class InvalidImageError(Exception):
    """
    Exception raised when the provided image is invalid.

    Args:
        message (str): The error message.

    Attributes:
        name (str): The name of the exception.
    """
    def __init__(self, message):
        super().__init__(message)
        self.name = "InvalidImageError"

class CarmenAPIError(Exception):
    """
    Exception raised when an API call fails: a non-2xx response, or a request
    that still fails after the configured number of retries.

    Attributes:
        name (str): The name of the exception.
        status (Optional[int]): The HTTP status code, when the API responded.
        body: The parsed response body, when the API responded.
    """
    def __init__(self, message, status=None, body=None):
        super().__init__(message)
        self.name = "CarmenAPIError"
        self.status = status
        self.body = body
