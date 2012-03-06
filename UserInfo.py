"""
	UserInfo.py -- Grabs user info from the database.
	
	by Sean.
"""

from Config import Config
from pymongo import Connection
from datetime import datetime
import time
import base64

class UserInfo:
	def __init__( self, config ):
		self.config = Config( config )
		
		self.address = self.config['mongo']['address']
		self.port = self.config['mongo']['port']
		
		self.database = "foodlisting"
		
		try:
			self.database = self.config['mongo']['database']
		except:
			pass
		
		self.collection = "users"
		
		try:
			self.collection = self.config['mongo']['user_collection']
		except:
			pass
		
		self.con Connection( self.address, self.port )
		
		self.db = self.con[self.database]
		self.collection = self.db[self.collection']
		
		self.collection.ensure_index( '