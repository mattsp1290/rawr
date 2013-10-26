from google.appengine.ext import db

class Rawr(db.Model):
	user = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)