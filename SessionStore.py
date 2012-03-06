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
		
	def addSession( self, sessionName ):
		session = {}
		session['name'] = sessionName
		session['id'] = b64encode( str( sha256( sessionName + str( datetime.now() ) ).digest ) )[:5]
		
		session['users'] = []
		session['stateDate'] = datetime.now()
		session['receipt'] = []
		session['tax'] = 0.0
		session['total'] = 0.0
		session['tip'] = 0.0
		session['paymentType'] = []
		
		self.collection.save( session )
		
		return session['id']
		
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
	
if __name__ == "__main__":
	from UserStore import UserStore
	s = SessionStore( "config.json" )
	u = UserStore( "config.json" )
	
	user = u.getByID( "1234567890" )
	
	sess = s.addSession( "test_session" )
	
	print sess
	print s.addUser( sess, user['uid'] )
	print s.get( sess )
	
	