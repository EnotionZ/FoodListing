"""
	UserInfo.py -- Grabs user info from the database.
	
	by Sean.
"""

from Config import Config
from pymongo import Connection
from datetime import datetime
import time
from hashlib import sha256
from base64 import b64encode

import logging

class UserStore:
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
		
		self.con = Connection( self.address, self.port )
		
		self.db = self.con[self.database]
		self.collection = self.db[self.collection]
		
		self.food = self.db['food']
		
		#self.collection.ensure_index( "id", unique=True )
		
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
	def addUser( self, id, idType, name, password, age, zip, loc ):
		user = {}
		user['uid'] 			= id	#user id
		user['idType'] 			= idType#id type, facebook, google, ect...
		user['food_history'] 	= []	#all food ordered by this person
		user['name'] 			= name	#name of the user
		user['pass']			= b64encode( sha256( password ).digest() )
		user['age'] 			= age	#age of the person
		user['location'] 		= loc	#location
		user['zip']				= zip	#zip code
		
		if self.collection.save( user ) != None:
			return user['uid']
		else:
			return None
	"""
		PRE: id = the users id
		POST: The RV is the user document or None if it does not exist.
	"""
	def getByID( self, id ):
		user = self.collection.find_one( { "uid": id } )
		user['_id'] = str( user['_id'] )
		
		history = user['food_history']
		
		food = []
		
		for h in history:
			h['date'] = str( h['date'] )
			f = self.food.find_one( { "_id": h['fid'] } )
			if not f == None:
				try:
					f['_id'] = str( f['_id'] )
					f['date'] = str( f['date'] )
					food.append( f )
				except:
					print f
			
		user['food_history'] = food
		
		return user
		
	"""
		PRE: username and password are defined.
		POST: The RV is not none if the user and password combination work.
	"""
	def checkUser( self, username, password ):
		p = b64encode( sha256( password ).digest() )
		return self.collection.find_one( { "name": username, "pass": p } )
		
	def addFood( self, id, fid ):
		food = { "fid": fid, "date": datetime.now() }
		return self.collection.update( { "uid": id }, { "$push": { "food_history": food } } )
		
if __name__ == "__main__":
	u = UserStore( "config.json" )
	
	a = u.addUser( "12345543215", "facebook", "Megan", "password", 21, 20151, ( 73.1, 73.1 ) )
	
	a = u.getByID( a )
	
	print a