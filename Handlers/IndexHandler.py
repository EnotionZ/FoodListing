"""
	IndexHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class IndexHandler( tornado.web.RequestHandler ):

	def get( self, action ):
		if action == "home":
			self.render( "templates/index.html" )
		elif action == "about":
			self.render( "templates/about.html" )
		elif action == "contact":
			self.render( "templates/contact.html" )
