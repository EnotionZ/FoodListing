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
	# 127.0.0.1:8080/rest/sessions/mR73w	
	def get( self, collection, action, param ):
	
		ret = {}
	
		if collection == "users":
			ret['data'] = handle_users( action, param )
		elif collection == "sessions":
			ret['data'] = handle_sessions( action, param )
		elif collection == "restaurant":
			ret['data'] = handle_restaurants( action, param )
		elif collection == "food":
			ret['data'] = handle_food( action, param )
		
		self.write( ret )
		
	def handle_users( action, param ):
		if action == "pull":
			user = self.users.getById( param )
			return user
			
	def handle_sessions( action, param ):
		if action == "pull":
			sess = self.sessions.getById( param )
			return sess

	def handle_restaurants( action, param ):
		if action == "pull":
			restaurant = self.restaurants.getByID
			return restaurant
			
	def handle_food( action, param ):
		if action == "pull":
			food = self.food.getById( param )
			return food
		