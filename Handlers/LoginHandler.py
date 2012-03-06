"""
	LoginHandler.py -- Handlers the login process.
	
	by Sean
"""

import tornado.web

class LoginHandler( tornado.web.RequestHandler ):
	
	def initialize( self, users ):
		self.users = users
	
	def get( self, action ):
		
