"""
	IndexHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class IndexHandler( tornado.web.RequestHandler ):
	def initialize( self, users, sessions, food ):
		self.users = users
		self.sessions = sessions
		self.food = food

	def get( self, action, param ):
		if action == "user":
			ret = self.users.getById( param )
			self.write( ret )
		elif action == "session":
			ret = self.sessions.getSession( id )
			self.write( ret )
