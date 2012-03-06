"""
	IndexHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class IndexHandler( tornado.web.RequestHandler ):
	
	def get( self ):
		self.render( "templates/index.html" )
