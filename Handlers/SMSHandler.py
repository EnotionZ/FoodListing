"""
	SMSHandler.py -- Sends text messages
"""

import tornado.web

from Config import Config
from twilio.rest import TwilioRestClient

class SMSHandler( tornado.web.RequestHandler ):
	def initialize( self, config ):
		self.config = Config( config )
		
		self.account = self.config['sms']['account']
		self.token = self.config['sms']['token']
		self.fromNum = self.config['sms']['fromNum']
		
	def post( self ):
		number = self.get_argument( "number", "" )
		message = self.get_argument( "message", "" )
		
		client = TwilioRestClient(self.account, self.token)

		message = client.sms.messages.create(to=number, from_=self.fromNum,
											 body=message)
											 
		if message:
			self.write( "OK" )
		else:
			self.write( "ERROR" )