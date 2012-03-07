"""
	Dashboard.py -- Handling the panels and information control and content displaying
	
	by Sean
"""

import tornado.web

class DashboardHandler( tornado.web.RequestHandler ):
	def initialize( self, users, sessions, restaurants ):
		self.users 			= users
		self.sessions 		= sessions
		self.restaurants 	= restaurants
		
	def get_login_url( self ):
		return "/login"
		
	def get_current_user( self ):
		user = self.get_secure_cookie( "user" )
		
		if user:
			return user
		else:
			None
		
	@tornado.web.authenticated
	def get( self, action ):
		print "hello"
		self.render( "templates/dashboard.html", page_title = "Dashboard", page_subtitle = "" )

	@tornado.web.authenticated
	def post( self, action ):
		self.render( "templates/dashboard.html",
					page_title = "Dashboard"
				)