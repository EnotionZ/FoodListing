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
		self.address = config['http']['bindaddress']
		self.port = config['http']['port']
		self.handlers = []
		
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
		self.application = self.load_handlers( config['http']['handlers'] );
		
	def load_handlers( self, handlers ):
		for h in handlers:
			self.handlers.append( ( h['regex'], eval( h['name'] ) ) )

		self.handlers.append( ( "/static/(.*)", StaticFileHandler, {
			"path": "public/"
			}))
	
	def run( self ):
		self.logger.info( "Creating application" )
		application = tornado.web.Application( self.handlers, debug=True );
		http = tornado.httpserver.HTTPServer( application )
		self.logger.debug( "Listening on: " + str( self.port ) )
		http.listen( self.port )
		self.logger.info( "Starting server" )
		tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	http = HttpServer( "config.json" )
	
	http.run()
