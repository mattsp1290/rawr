from google.appengine.ext import db

class Rawr(db.Model):
	user = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)
	
	@classmethod
	def rawr_key(cls, name = 'default'):
		return db.Key.from_path('rawrs', name)
