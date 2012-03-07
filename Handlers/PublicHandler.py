"""
	IndexHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class PublicHandler( tornado.web.RequestHandler ):

	def get( self, action ):
		print action
		if action in [ "/", "/home", "" ]:
			self.render( "templates/index.html", 
					page_title="Dashboard",
					page_subtitle="subtitle for dashboard")
		elif action == "/about":
			self.render( "templates/about.html" )
		elif action == "/contact":
			self.render( "templates/contact.html" )
