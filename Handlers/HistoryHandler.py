"""
	IndexHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class PublicHandler( tornado.web.RequestHandler ):

	def get( self ):
		self.render( "templates/historu.html" )
