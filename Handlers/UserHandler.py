"""
	UserHandler.py -- Performs the nesscary user interaction handling.
	
	by Sean
"""

import tornado.web

class UserHandler( tornado.web.RequestHandler ):
	def initialize( self, users ):
		self.users = users
		
	@tornado.web.authenticated
	def get( self, action ):
		self.render( "templates/userpage.html" )
		
	@tornado.web.authenticated
	def post( self, action ):
		self.render( "templates/userpage.html" )