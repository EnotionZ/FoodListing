"""
	RedirectHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class RedirectHandler( tornado.web.RequestHandler ):
		
	def get( self ):
		self.redirect( "/home" )
