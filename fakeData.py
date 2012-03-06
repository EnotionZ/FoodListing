"""
	Create a lot of fake data to enter into the data base
"""

from random import randint
from numpy.random import random_integers
from numpy.random import random_sample

from UserStore import UserStore
from SessionStore import SessionStore
from ReceiptStore import ReceiptStore
from FoodStore import FoodStore
sessions = SessionStore( "config.json" )
users = UserStore( "config.json" )
receipts = ReceiptStore( "config.json" )
foods = FoodStore( "config.json" )

numSessions = randint( 10, 20 )

#numUsers = randint( 20, 50 )

#for u in range( numUsers ):
#	lat = random_sample( 2 )
#	lat = ( lat[0], lat[1] )
#	users.addUser( str( randint( 1, 1000000 ) ), 
#					"facebook", 
#					str( randint( 1, 1000000 ) ),
#					randint( 18, 35 ),
#					lat )
MENU = [ "pizza", "pasta", "bread", "pie", "steak", "hippies" ]
us = users.collection.find()
ut = []
for u in us:
	ut.append( u['uid'] )
	
print numSessions
	
for sess in range( numSessions ):
	users = random_integers( 0, len( ut ) - 1, randint( 1, 5 ) )
	
	id = sessions.addSession( str( randint( 1, 1000000000000000 ) ) )
	
	for i in users:
		sessions.addUser( id, ut[i] )
		
		fid = foods.addFood( ut[i], MENU[randint( 0, len( MENU )	 ) - 1], id, ( 0, 0 ) )
		
		sessions.addFood( id, fid )
		

		
		
		
	