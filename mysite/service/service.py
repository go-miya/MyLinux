from tornado.web import Application
import tornado.ioloop
import tornado.httpserver
from app import app

class App(Application):
    def __init__(self):
        handlers = [
            (r'/xing/helloworld', app.HelloWorld),
            (r'/xing/suibi', app.SuiBi),
        ]
        super(App, self).__init__(handlers=handlers)


def start_http(port):
    io_loop = tornado.ioloop.IOLoop.instance()
    application = App()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    io_loop.start()

