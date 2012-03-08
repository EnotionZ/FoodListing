"""
	HttpServer.py -- This is the httpd server, configurable from config.json
	
	by Sean
"""

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from Handlers import *
from tornado.web import StaticFileHandler
from Config import Config
import re
import logging
from base64 import b64encode
import uuid
from pymongo import Connection
from UserStore import UserStore
from SessionStore import SessionStore
from RestaurantStore import RestaurantStore
from FoodStore import FoodStore

LEVELS = {
			'debug': logging.DEBUG,
			'info': logging.INFO,
			'warning': logging.WARNING,
			'error': logging.ERROR,
			'critical': logging.CRITICAL
		}

class HttpServer:
	def __init__( self, configFile ):
		config = Config( configFile )
		self.configFile = configFile
		self.address = config['http']['bindaddress']
		self.port = config['http']['port']
		self.handlers = []
		
		self.con = Connection( config['mongo']['address'], config['mongo']['port'] )
		
		self.users = UserStore( configFile )
		self.sessions = SessionStore( configFile )
		self.restaurants = RestaurantStore( configFile )
		self.foods = FoodStore( configFile )
		
		console = logging.StreamHandler()
		formatter = logging.Formatter('%(asctime)s: %(name)s - %(levelname)s - %(message)s')
		console.setFormatter( formatter )
		logging.getLogger('').addHandler( console )
		self.logger = logging.getLogger( "HttpServer" )
		self.logger.debug( "HttpServer Started" )
		
		try:
			self.logger.setLevel( LEVELS[self.config['logLevel']] )
		except:
			self.logger.setLevel( logging.ERROR )
		
		self.logger.info( "Loading page handelrs" )
	
	def run( self ):
		settings = {
			"cookie_secret": b64encode( uuid.uuid4().bytes + uuid.uuid4().bytes ), 
			"login_url": "/login",
			"debug": True
		}
		self.logger.info( "Creating application" )
		application = tornado.web.Application( 
		[
			( r"/", RedirectHandler ),
			( r"/login", LoginHandler, dict( users = self.users, ) ),
			( r"/dashboard(/\w*)?", DashboardHandler, dict( users = self.users, sessions = self.sessions, restaurants = self.restaurants, ) ),
			( r"/home(/?\w*)", PublicHandler ),
			( r"/static/(.*)", StaticFileHandler, { "path": "public/" }),
			( r"/rest/(\w+)/([\w\d]+)/([\w\d]+)", RestHandler, dict( users = self.users, sessions = self.sessions, restaurants = self.restaurants, food = self.foods, ) ),
			( r"/m/(.*)", StaticFileHandler, { "path": "mobile/" } ),
			( r"/sms", SMSHandler, dict( config = self.configFile, ) )
			#( r"/shorten", ShortenHandler, dict( config = self.configFile ) )
		], **settings )
		http = tornado.httpserver.HTTPServer( application )
		self.logger.debug( "Listening on: " + str( self.port ) )
		http.listen( self.port )
		self.logger.info( "Starting server" )
		tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	http = HttpServer( "config.json" )
	
	http.run()
