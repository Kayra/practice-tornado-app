from tornado.options import define, options
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.ioloop import IOLoop


define('port', default=8888, help='This is the port to listen on.')


def main():
    """
    Construct and serve the tornado application.
    """

    app = Application()
    http_server = HTTPServer(app)
    http_server.listen(options.port)

    print(f"Listening on http:127.0.0.1:{options.port}")

    IOLoop.current().start()
