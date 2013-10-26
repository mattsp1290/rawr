from handlers.base import AppHandler
from google.appengine.api import memcache
from models.rawr import Rawr
import logging
import time

class RawrHandler(AppHandler):
	def get(self, post_id):
		if not memcache.get(post_id):
			logging.error("Running DB Query")
			value = {'time': time.time(), 'rawr': Rawr.get_by_id(int(post_id))}
			memcache.set(post_id, value)
		value = memcache.get(post_id)
		rawr = value['rawr']
		self.values['rawr_user'] =  str(rawr.user)
		self.values['content'] = str(rawr.content)
		self.values['submitted'] = rawr.created
		self.render('rawr.html')