"""
	IndexHandler.py -- Handlers index page interactions.
	
	by Sean
"""

import tornado.web

class RestHandler( tornado.web.RequestHandler ):
	def initialize( self, users, sessions, restaurants, food ):
		self.users = users
		self.sessions = sessions
		self.food = food
		self.restaurants = restaurants
		
	def get( self, collection, action, param ):
		if collection == "users":
			handle_users( action, param )
		elif collection == "sessions":
			handle_sessions( action, param )
		elif collection == "restaurant":
			handle_restaurants( action, param )
		elif collection == "food":
			handle_food( action, param )
	
	def handle_users( action, param ):
		pass
		
	def handle_sessions( action, param ):
		pass

	def handle_restaurants( action, param ):
		pass
		
	def handle_food( action, param ):
		pass