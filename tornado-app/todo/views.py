from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    """
    A request handler that responds with 'Hello world'
    """

    def get(self):
        self.write("Hello world")
