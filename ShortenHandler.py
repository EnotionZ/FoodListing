"""
	ShortenHandler.py -- Handles shortening of links.
	
	by Sean
"""

import tornado.web

from Config import Config

from bitly import *

class ShortenHandler( tornado.web.RequestHandler ):
	def initialize( self, config ):
		self.config = Config( config )
		
		self.apikey = self.config['bitly']['apikey']
		self.user = self.config['bitly']['user']
		
	def post( self ):
		a = Api( login=self.user, apikey=self.apikey )
		url = self.geT_arguement( "url", "" )
		
		self.write( a.shorten( url ) )