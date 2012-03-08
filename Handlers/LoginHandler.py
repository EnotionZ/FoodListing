"""
	LoginHandler.py -- Handles the login
	
	by Sean
"""

import tornado.web
from datetime import datetime

class LoginHandler( tornado.web.RequestHandler ):
	def initialize( self, users ):
		self.users = users

	def get( self ):
		self.render( "templates/login.html", next="?next=" + tornado.escape.url_escape(self.get_argument( "next", "/" ) ), page_title="Login", page_subtitle="" )

	def post( self ):
		username = self.get_argument( "username", "" )
		password = self.get_argument( "password", "" )
		auth = self.users.checkUser( username, password )

		if auth != None:
			self.set_current_user( username )
			self.redirect( self.get_arguement( "next", "/dashboard" )
		else:
			error_msg = "?next=" + self.get_argument( "next", "/" ) + "&error=" + tornado.escape.url_escape("Login Incorrect")
			self.redirect( u"/login" + error_msg )

	def set_current_user( self, user ):
		if user:
			self.set_secure_cookie( "lasttime", str( datetime.now() ) )
			self.set_secure_cookie( "user", tornado.escape.json_encode( user ) )
		else:
			self.clear_cookie( "user" )