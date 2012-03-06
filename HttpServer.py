"""
	HttpServer.py -- This is the httpd server, configurable from config.json
	
	by Sean
"""

import tornado.ioloop
import tornado.web
from Handlers import *
from Config import Config
import re

class HttpServer:
	def __init__( self, configFile ):
		config = Config( configFile )
		self.address = config['http']['bindaddress']
		self.port = config['http']['port']
		self.handlers = []
		self.application = self.load_handlers( config['http']['handlers'] );
		
		try:
			if config['http']['debug'] == True:
				self.debug = True
			else:
				self.debug = False
		except:
			self.debug = false
		
	def load_handlers( self, handlers ):
		for h in handlers:
			self.handlers.append( ( h['regex'], eval( h['name'] ) ) )
	
	def run( self ):
		application = tornado.web.Application( self.handlers, debug=self.debug );
		application.listen( int( self.port ) )
		http = tornado.httpserver.HTTPServer( application )
		http.listen( self.port )
		tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	http = HttpServer( "test.json" )
	
	http.run()
