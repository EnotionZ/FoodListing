"""
	IndexHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class PublicHandler( tornado.web.RequestHandler ):

	def get( self, action ):
		print action
		if action in [ "/", "/public", "" ]:
			self.render( "templates/index.html")
		elif action == "/about":
			self.render( "templates/about.html")
		elif action == "/team":
			self.render( "templates/team.html" )
