from handlers.base import AppHandler
from models.user import User
from models.rawr import Rawr
from google.appengine.api import memcache
import logging
import time

class HomeHandler(AppHandler):
	def get(self):
		if not memcache.get('front_rawrs'):
			self.set_front_page()
		self.render_page()
		
	def post(self):
		content = self.request.get('content')
		username = self.request.get('username')
		if (len(content) > 0) and (len(content) < 257):
			rawr = Rawr(content=content, user=username)
			rawr.put()
			self.values['content'] = None
			self.set_front_page()
			self.redirect("/")
		else:
			errors = "Rawrs must be 256 characters or less"
			self.render_page(content, errors)
		
	def render_page(self, content="", errors=None):
		self.values['content'] = content
		self.values['errors'] = errors
		self.values['rawrs'] = memcache.get('front_rawrs')
		self.render('home.html')
		
	def set_front_page(self):
		logging.error("Running DB Query")
		memcache.set('front_rawrs', Rawr.all().order('-created').fetch(25))