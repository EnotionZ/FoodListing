""" 
	SessionStore.py -- Stores session information and helps to regulate the sessions of users
		for their current food eating session.
		
	by Sean.
"""
from Config import Config
from pymongo import Connection
from hashlib import sha256
from base64 import b64encode
import logging
from datetime import datetime

class SessionStore:
	def __init__( self, config ):
		self.config = Config( config )
		
		self.address = self.config['mongo']['address']
		self.port = self.config['mongo']['port']
		
		self.database = "foodlisting"
		
		try:
			self.database = self.config['mongo']['database']
		except:
			pass
			
		self.collection = "sessions"
			
		self.con = Connection( self.address, self.port )
		self.db = self.con[self.database]
		self.collection = self.db[self.collection]
		self.collection.ensure_index( "id", unique=True )
		
	def addSession( self, sessionName, restaurantId ):
		session = {}
		session['name'] = sessionName						#Restaurant Name
		name = sessionName + str( datetime.now() )			
		session['id'] = b64encode( sha256( name ).digest() )[:5].replace( "/", "1" )			#restaunrant name and date
		session['users'] = []								#Array of current users in session.
		session['stateDate'] = datetime.now()				#when did this session start.
		session['receipt'] = []								#Array of food items
		session['tax'] = 0.0								#Tax percent
		session['total'] = 0.0								#Total cost
		session['tip'] = 0.0								#Tip percent.
		session['paymentType'] = []		#What methods were used to pay.
		session['restaurantId'] = restaurantId
		self.collection.save( session )
		
		return session['id']
		
	def addFood( self, id, fid ):
		self.collection.update( { "id": id }, { "$push": { "receipt": fid } } )
	def get( self, id ):
		return self.collection.find_one( { "id": id } )
		
	def addUser( self, id, userid ):
		return self.collection.update( { "id": id }, { "$addToSet": { "users": userid } } )
		
	def addReceipt( self, id, receiptId ):
		session = self.get( id )
		
		ret = None
		
		if session != None and session['receipt'] == None:
			session['receipt'] = receiptId
			self.collection.save( session )
			ret = session['id']
		return ret
		
	def setTaxRate( self, id, taxrate ):
		return self.collection.update( { "id": id }, { "tax": taxrate } )
		
	def setTotal( self, id, total ):
		return self.collection.update( { "id": id }, { "total": total } )
	
	def setTip( self, id, tip ):
		return self.collection.update( { "id": id }, { "tip": tip } )
		
	def addPaymentType( self, id, payment ):
		return self.collection.update( { "id": id }, { "$addToSet": { "paymentType": payment } } )
		
	def getById( self, id ):
		return self.collection.find_one( { "id": id } )
		
	#This is based on the number of sessions at the restaurant not people
	def getNumberOfVisitsRestaurant( self, id ):
		return self.db.sessions.find( { "restaurant": id } ).count()
	
	#how much food was ordered here?
	def getFoodCountsRestaurant( self, id ):
		sessions = self.collection.find( { "restaunrant": id } )
		
		food = {}
		
		for s in sessions:
			for f in s['receipt']:
				a = self.db.food.find_one( { "id": f['id'] } )
				
				if a['name'] in food:
					food[a['name']]['count'] += 1
				else:
					food[a['name']]['count'] = 1
					food[a['name']]['food'] = a

		return food
	
if __name__ == "__main__":
	from UserStore import UserStore
	s = SessionStore( "config.json" )
	u = UserStore( "config.json" )
	
	user = u.getByID( "1234567890" )
	
	sess = s.addSession( "test_session" )
	
	print sess
	print s.addUser( sess, user['uid'] )
	print s.get( sess )
	
	