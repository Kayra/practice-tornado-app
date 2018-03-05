from datetime import datetime
import json

from tornado_sqlalchemy import SessionMixin, as_future
from tornado.web import RequestHandler
from tornado.gen import coroutine

from todo.models import User, Task


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


class TaskListView(BaseView):
    """
    View for reading and adding new tasks
    """

    SUPPORTED_METHODS = ["GET", "POST"]

    @coroutine
    def get(self, username):
        """
        Get all tasks for an existing user
        """

        with self.make_session() as session:
            user = yield as_future(session.query(User).filter(User.username == username).first)
            if user:
                tasks = [task.to_dict() for task in user.tasks]
                self.send_response({
                    'username': user.username,
                    'tasks': tasks
                })

    @coroutine
    def post(self, username):
        """
        Creates a new task
        """

        with self.make_session() as session:

            user = yield as_future(session.query(User).filter(User.username).first)
            if user:

                due_date = self.data['due_date'][0]

                task = Task(
                    name=self.data['name'][0],
                    note=self.data['note'][0],
                    creation_date=datetime.now(),
                    due_date=datetime.strptime(due_date, '%d/%m/%Y %H:%M:%S') if due_date else None,
                    completed=self.data['completed'][0],
                    user_id=user.id,
                    user=user
                )

                session.add(task)
                self.send_response({'message': 'posted'}, status=201)


class ListRoutesView(RequestHandler):
    """
    View for listing available routes
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
