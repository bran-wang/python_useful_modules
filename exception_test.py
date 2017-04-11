import logging

LOG = logging.getLogger(__name__)


class BaseException(Exception):
    """The Base Exception to extend custom exceptions.

    The Base Exception to extend your exception classes. The user
    should define a message property.
    """
    message = "An Unknown exception occurred."

    def __init__(self, msg=None, **kwargs):
        if msg:
            self.message = msg
        if kwargs:
            try:
                self.msg = self.message % kwargs
            except Exception as e:
                LOG.warning("Exception formatting error: %(e)s. Message: "
                            "%(msg)s. kwargs: %(kwargs)s",
                            {'e': e, 'msg': self.message, 'kwargs': kwargs})
                self.msg = self.message
        else:
            self.msg = self.message
        super(BaseException, self).__init__(self.msg)


class Invalid(BaseException):
    message = "An invalid input was detected."


class NotFound(BaseException):
    message = "The resource was not found on the server."
