from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, Application
from app import app

tr = WSGIContainer(app)

application = Application([
(r".*", FallbackHandler, dict(fallback=tr)),
])

if __name__ == "__main__":
  application.listen(80)
  IOLoop.instance().start()
