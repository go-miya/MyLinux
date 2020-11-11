import tornado.ioloop
import tornado.web
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(make_app())
    server.bind(8888)
    server.start(0)  # Forks multiple sub-processes
    tornado.ioloop.current().start()