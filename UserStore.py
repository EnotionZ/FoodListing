"""
	UserInfo.py -- Grabs user info from the database.
	
	by Sean.
"""

from Config import Config
from pymongo import Connection
from datetime import datetime
import time
import base64

import logging

class UserInfo:
	def __init__( self, config ):
		self.config = Config( config )
		
		self.address = self.config['mongo']['address']
		self.port = self.config['mongo']['port']
		
		self.database = "foodlisting"
		
		self.logger = logging.getLogger( "FoodListing.DB.UserInfo" )
		
		try:
			self.database = self.config['mongo']['database']
		except:
			pass
		
		self.collection = "users"
		
		try:
			self.collection = self.config['mongo']['user_collection']
		except:
			pass
		
		self.con = Connection( self.address, self.port )
		
		self.db = self.con[self.database]
		self.collection = self.db[self.collection]
		
		self.collection.ensure_index( 'id', unique=True )
		
	"""
		PRE: uid = fb, google, other id
			name = user's real name gathered from their account
					upon registration.
			age = user's real age gathered from their account 
					upon registration.
			loc = 2-tuple that contains their approximate lat/lng.
					this can be gotten from facebook/google or guess
					from their registration ip.
		POST: The user with the above information is added,
			and the object is returned from the function to be used
			else where.
	"""
	def addUser( self, id, idType, name, age, loc ):
		user = {}
		user['id'] = id
		user['idType'] = idType
		user['food_history'] = []
		user['name'] = name
		user['age'] = age
		user['location'] = loc
		
		return self.collection.save( user )
		
	def getUserByID( self, id ):
		user = self.collection.find_one( { "_id": id } )
		
		return user
		
if __name__ == "__main__":
	u = UserInfo( "config.json" )
	
	a = u.addUser( "12345678910", "test", 21, ( 73.1, 73.1 ) )
	
	a = u.getUserByID( a )
	
	print a