from handlers.base import AppHandler
from models.rawr import Rawr

class NewRawrHandler(AppHandler):
	def get(self):
		self.render_form()
		
	def post(self):
		content = self.request.get('content')
		if (len(subject) > 0) and (len(content) > 0):
			rawr = Rawr(subject=subject, content=content)
			rawr.put()
			self.redirect("/" + str(rawr.key().id()))
		else:
			errors = "Rawrs must be 256 characters or less"
			self.render_form(content, errors)
		
	def render_form(self, subject="", content="", errors=None):
		self.values['content'] = content
		self.values['errors'] = errors
		self.render('post_form.html')