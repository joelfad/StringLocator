#
# StringLocator - 24 hour programming challenge
#
# [invalidusage.py]
# Exception definitions used for error handling
# (source: http://flask.pocoo.org/docs/0.12/patterns/apierrors/)
#

class InvalidUsage(Exception):

    # default
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        """
        Create

        :param message: string, description of failure
        :param status_code: int, REST status code (e.g. 400, 401, 404, etc.)
        :param payload: dictionary, data to send in error response
        """
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """
        Represent exception as a dictionary
        """
        d = dict(self.payload or ())
        d['message'] = self.message
        return d
