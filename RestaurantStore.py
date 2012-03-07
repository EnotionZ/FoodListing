"""
	UserInfo.py -- Grabs user info from the database.
	
	by Sean.
"""

from Config import Config
from pymongo import Connection
from datetime import datetime
import time
from base64 import b64encode
from hashlib import sha256

import logging

class RestaurantStore:
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
		
		self.collection = "restaurants"
		
		self.con = Connection( self.address, self.port )
		
		self.db = self.con[self.database]
		self.collection = self.db[self.collection]
		
		self.collection.ensure_index( "id", unique=True )
		
	def addRestaurant( self, name, location ):
		restaurant = {}
		restaurant['name'] 	= name									#Name of the place
		restaurant['id'] 	= b64encode( sha256( name ).digest() )[:5].replace( "/", "1" )
		restaurant['menu'] 	= []									#menu of food items
		restaurant['loc'] 	= location								#location
		
		if self.collection.save( restaurant ) != None:
			return restaurant['id']
		else:
			return None

	def getByID( self, id ):
		restaurant = self.collection.find_one( { "id": id } )
		
		return restaurant
		
	def addMenuItem( self, id, fid ):
		return self.collection.update( { "id": id }, { "$addToSet": { "menu": fid } } )
		
	def getMenu( self, id ):
		ret = self.collection.find_one( { "id": id } )
		
		return ret['menu']
		
if __name__ == "__main__":
	u = RestaurantStore( "config.json" )
	
	a = u.addRestaurant( "Out Back Steak House", ( 73.1, 73.1 ) )
	
	a = u.getByID( a )
	
	print a