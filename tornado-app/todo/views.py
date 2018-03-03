import json

from tornado_sqlalchemy import SessionMixin
from tornado.web import RequestHandler


class BaseView(RequestHandler, SessionMixin):
    """
    Base view for this application
    """

    def prepare(self):
        """
        Convert byte string to unicode for use in the view
        """
        self.data = {
            key: [value.decode('utf-8') for value in value_list]
            for key, value_list in self.request.arguments.items()
        }

    def set_default_headers(self):
        """
        Set the default response header to be JSON
        """
        self.set_header("Content-Type",
                        "application/json; charset=\"utf-8\"")

    def send_response(self, data, status=200):
        """
        Construct and send a JSON response with appropriate status code.
        """

        self.set_status(status)
        self.write(json.dumps(data))



class ListRoutesView(RequestHandler):
    """
    Only allow GET requests.
    """

    SUPPORTED_METHODS = ["GET"]

    def set_default_headers(self):
        """
        Set the default response header to be JSON
        """
        self.set_header("Content-Type",
                        "application/json; charset=\"utf-8\"")

    def get(self):
        """
        List of routes for this API
        """

        routes = {
            'info': 'GET /api/v1',
            'register': 'POST /api/v1/accounts',
            'single profile detail': 'GET /api/v1/accounts/<username>',
            'edit profile': 'PUT /api/v1/accounts/<username>',
            'delete profile': 'DELETE /api/v1/accounts/<username>',
            'login': 'POST /api/v1/accounts/login',
            'logout': 'GET /api/v1/accounts/logout',
            "user's tasks": 'GET /api/v1/accounts/<username>/tasks',
            "create task": 'POST /api/v1/accounts/<username>/tasks',
            "task detail": 'GET /api/v1/accounts/<username>/tasks/<id>',
            "task update": 'PUT /api/v1/accounts/<username>/tasks/<id>',
            "delete task": 'DELETE /api/v1/accounts/<username>/tasks/<id>'
        }

        self.write(json.dumps(routes))


class HelloWorld(RequestHandler):
    """
    A request handler that responds with 'Hello world'
    """

    def get(self):
        self.write("Hello world")