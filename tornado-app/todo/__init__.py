import os

from tornado_sqlalchemy import make_session_factory
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.ioloop import IOLoop

from todo.views import HelloWorld, ListRoutesView


define('port', default=8888, help='This is the port to listen on.')
factory = make_session_factory(os.environ.get('DATABASE_URL', 'postgres://localhost:5432/tornado_todo'))


def main():
    """
    Construct and serve the tornado application.
    """

    app = Application([
        ('/', ListRoutesView),
        ('/hi', HelloWorld)
    ],
        session_factory=factory
    )

    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print(f"Listening on http://127.0.0.1:{options.port}/")

    IOLoop.current().start()
