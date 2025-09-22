class SegmentError(Exception):
    """class representing Generic Http error."""

    def __init__(self, message=None, response=None):
        super().__init__(message)
        self.message = message
        self.response = response


class SegmentBackoffError(SegmentError):
    """class representing backoff error handling."""
    pass

class SegmentBadRequestError(SegmentError):
    """class representing 400 status code."""
    pass

class SegmentUnauthorizedError(SegmentError):
    """class representing 401 status code."""
    pass


class SegmentForbiddenError(SegmentError):
    """class representing 403 status code."""
    pass

class SegmentNotFoundError(SegmentError):
    """class representing 404 status code."""
    pass

class SegmentConflictError(SegmentError):
    """class representing 409 status code."""
    pass

class SegmentUnprocessableEntityError(SegmentBackoffError):
    """class representing 422 status code."""
    pass

class SegmentRateLimitError(SegmentBackoffError):
    """class representing 429 status code."""
    pass

class SegmentInternalServerError(SegmentBackoffError):
    """class representing 500 status code."""
    pass

class SegmentNotImplementedError(SegmentBackoffError):
    """class representing 501 status code."""
    pass

class SegmentBadGatewayError(SegmentBackoffError):
    """class representing 502 status code."""
    pass

class SegmentServiceUnavailableError(SegmentBackoffError):
    """class representing 503 status code."""
    pass

ERROR_CODE_EXCEPTION_MAPPING = {
    400: {
        "raise_exception": SegmentBadRequestError,
        "message": "A validation exception has occurred."
    },
    401: {
        "raise_exception": SegmentUnauthorizedError,
        "message": "The access token provided is expired, revoked, malformed or invalid for other reasons."
    },
    403: {
        "raise_exception": SegmentForbiddenError,
        "message": "You are missing the following required scopes: read"
    },
    404: {
        "raise_exception": SegmentNotFoundError,
        "message": "The resource you have specified cannot be found."
    },
    409: {
        "raise_exception": SegmentConflictError,
        "message": "The API request cannot be completed because the requested operation would conflict with an existing item."
    },
    422: {
        "raise_exception": SegmentUnprocessableEntityError,
        "message": "The request content itself is not processable by the server."
    },
    429: {
        "raise_exception": SegmentRateLimitError,
        "message": "The API rate limit for your organisation/application pairing has been exceeded."
    },
    500: {
        "raise_exception": SegmentInternalServerError,
        "message": "The server encountered an unexpected condition which prevented" \
            " it from fulfilling the request."
    },
    501: {
        "raise_exception": SegmentNotImplementedError,
        "message": "The server does not support the functionality required to fulfill the request."
    },
    502: {
        "raise_exception": SegmentBadGatewayError,
        "message": "Server received an invalid response."
    },
    503: {
        "raise_exception": SegmentServiceUnavailableError,
        "message": "API service is currently unavailable."
    }
}

