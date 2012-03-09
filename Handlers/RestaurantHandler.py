"""
	RestaurantHandler.py -- Handles the restaurant dashboard.
	
	by Sean
"""

import tornado.web

class RestaurantHandler( tornado.web.RequestHandler ):
	def initialize( self, restaurants, food, sessions, user ):
		self.restaurants = restaurants
		self.food = food
		self.sessions = sessions
		self.users = user
		
	def get( self, id ):
		restaurant = self.restaurants.getByID( id )
		
		self.render( "templates/restaurant.html", restaurant = restaurant )