"""
	LogoutHandler.py -- Handles the logout
	
	by Sean
"""

import tornado.web
from datetime import datetime

class LogoutHandler( tornado.web.RequestHandler ):
	def get( self ):
		self.clear_cookie("user")
		self.redirect("/")

