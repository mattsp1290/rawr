from handlers.base import AppHandler
from google.appengine.api import memcache


class FlushHandler(AppHandler):
    def get(self):
		memcache.flush_all()
		self.redirect("/")