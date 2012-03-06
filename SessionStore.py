""" 
	SessionStore.py -- Stores session information and helps to regulate the sessions of users
		for their current food eating session.
		
	by Sean.
"""

from pymongo import Connection
from hashlib import sha256
from base64 import b64encode
import logging

class SesstionStore:
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
		
		try:
			self.collection = self.config['mongo']['collection']
		except:
			pass
			
		self.con = Connection( self.address, self.port )
		self.db = self.con[self.database]
		self.collection = self.db[self.collection]
		self.collection.ensure_index( "id", unique=True )
		
	def addSession( self, sessionName ):
		session['name'] = sessionName
		session['id'] = b64encode( sha256( sessionName + str( datetime.now() ) ).digest )[:5]
		
		session['users'] = []
		session['stateDate'] = datetime.now()
		session['receipt'] = []
		session['tax'] = 0.0
		session['total'] = 0.0
		session['tip'] = 0.0
		session['paymentType'] = []
		
		return self.collection.save( session )
		
	def get( self, id ):
		return sefl.collection.findOne( { "id": id } )
		
	def addUser( self, id, userid ):
		session = self.geT( id )
		
		ret = None
		if session != None:
			session['users'].append( userid )
			ret = self.collection.save( session )
			
		return ret
		
	def addReceipt( self, id, receiptId ):
		session = self.get( id )
		
		ret = None
		
		if session != None and session['receipt'] == None:
			session['receipt'] = receiptId
			self.collection.save( session )
			
		return ret
		
	def setTaxRate( self, id, taxrate ):
		return self.collection.update( { "id": id }, { "tax": taxrate } )
		
	def setTotal( self, id, total ):
		return self.collection.update( { "id": id }, { "total": total } )
	
	def setTip( self, id, tip ):
		return self.collection.update( { "id": id }, { "tip": tip } )
		
	def addPaymentType( self, id, payment ):
		return self.collection.update( { "id": id }, { "$push": { "paymentType": payment } )
		
	
	