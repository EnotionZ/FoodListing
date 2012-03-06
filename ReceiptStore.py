"""
	ReceiptStore.py -- Handlers the mangement of the receipt objetcs.
	
	by Sean
"""

from pymongo import Connection
from Config import Config

class ReceiptStore:
	def __init__( self, config ):
		self.config = Config( config )
		
		self.address = self.config['mongo']['address']
		self.port = self.config['mongo']['port']
		
		self.database = "foodlisting"
		
		try:
			self.database = self.config['mongo']['database']
		except:
			pass
			
		self.collection = "receipt"
		
		self.con = Connection( self.address, self.port )
		self.db = self.con[self.database]
		self.collection = self.db[self.collection]
		
	def addReceipt( self, sessionid ):
		receipt = {}
		receipt['food'] = []
		receipt['session'] = sessionid
		
		return self.collection.save( receipt )
		
	def addFood( self, id, food ):
		return self.collection.update( { "_id": id }, { "$push" : { "food": food } } )
		
	def getReceipt( self, id ):
		return self.collection.find_one( { "_id": id } )
		
if __name__ == "__main__":
	from FoodStore import FoodStore
	r = ReceiptStore( "config.json" )
	f = FoodStore( "config.json" )
	
	p = f.getFoodByName( "pizza" )
	
	i = r.addReceipt( "PGJ1a" )
	
	r.addFood( i, p[0]["_id"] )
	
	print r.getReceipt( i )