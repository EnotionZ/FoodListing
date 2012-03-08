"""
	SMSHandler.py -- Sends text messages
"""

import tornado.web

from Config import Config
from twilio.rest import TwilioRestClient
import json

class SMSHandler( tornado.web.RequestHandler ):
	def initialize( self, config, sessions, foods ):
		self.config = Config( config )
		
		self.account = self.config['sms']['account']
		self.token = self.config['sms']['token']
		self.fromNum = self.config['sms']['fromNum']
		
		self.sessions = sessions
		self.foods = foods
		
	def post( self ):
		number = self.get_argument( "number", "" )
		message = self.get_argument( "message", "" )
		food = self.get_argument( "food", "" )
		food = json.dumps( food )
		
		foods = []
		
		for f in food['data']:
			f = self.foods.getByName( f['name'] )
			foods.append( f )
		
		client = TwilioRestClient(self.account, self.token)

		message = client.sms.messages.create(to=number, from_=self.fromNum, body=message)
											 
		if message:
			self.write( "OK" )
		else:
			self.write( "ERROR" )