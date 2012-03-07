"""
	FoodStore.py -- This provides an interface to the food items.
	
	by Sean
"""

from pymongo import Connection
from Config import Config
from datetime import datetime
class FoodStore:
	def __init__( self, config ):
		self.config = Config( config )
		
		self.address = self.config['mongo']['address']
		self.port = self.config['mongo']['port']
		
		self.database = "foodlisting"
		
		try:
			self.database = self.config['mongo']['database']
		except:
			pass
			
		self.collection = "food"
		
		self.con = Connection( self.address, self.port )
		self.db = self.con[self.database]
		self.collection = self.db[self.collection]
		
	def addFood( self, userid, name, cost, sessionid, restaurantId = None ):
		food = {}
		food['user'] 		= userid			#Who bought this?
		food['name'] 		= name				#Name of the food ie: pizza
		food['session'] 	= sessionid			#What session was this bought in?
		food['cost'] 		= cost				#What did it cost?
		food['date'] 		= datetime.now()	#When was thus food bought?
		food['restaurant'] 	= restaurantId		#What restaurant? Can be None
		
		return self.collection.save( food )
	
	def getFoodByName( self, name ):
		foods = self.collection.find( { "name": name } )
		
		ret = []
		
		for f in foods:
			ret.append( f )
			
		return ret
		
	def getFoodByUser( self, userid ):
		foods = self.collection.find( { "user": userid } )
		
		ret = []
		
		for f in foods:
			ret.append( f )
			
		return ret
		
	def getFoodBySession( self, session ):
		foods = self.collection.find( { "session": session } )
		
		ret = []
		
		for f in foods:
			ret.append( f )
			
		return ret
		
	def getFoodByTime( self, date ):
		foods = self.collection.find( { "time": date } )
		
		ret = []
		
		for f in foods:
			ret.append( f )
			
		return ret
		
	def getFoodByLoc( self, loc ):
		foods = self.collection.find( { "loc": loc } )
		
		ret = []
		
		for f in foods:
			ret.append( f )
			
		return ret
		
	def getFoodByName( self, name ):
		foods = self.collection.find( { "name": name } )
		
		ret = []
		
		for f in foods:
			ret.append( f )
			
		return ret
		
if __name__ == "__main__":
	f = FoodStore( "config.json" )
	
	
	print "Get food By name"
	print f.getFoodByName( "pizza" )
	print "get food By session"
	print f.getFoodBySession( "PGJ1a" )
	print "Get Food By Location"
	print f.getFoodByLoc( ( 73.1, 73.1 ) )
	