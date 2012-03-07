"""
	Create a lot of fake data to enter into the data base
"""

from random import randint
from numpy.random import random_integers
from numpy.random import random_sample

from UserStore import UserStore
from SessionStore import SessionStore
from FoodStore import FoodStore
from datetime import datetime
from RestaurantStore import RestaurantStore

sessions = SessionStore( "config.json" )
users = UserStore( "config.json" )
restaurant = RestaurantStore( "config.json" )
foods = FoodStore( "config.json" )


numSessions = randint( 10, 20 )

menu = restaurant.getMenu( "mGoPS" )

us = users.collection.find()
ut = []
for u in us:
	ut.append( u['uid'] )
	
print numSessions
	
for sess in range( numSessions ):
	us = random_integers( 1, len( ut ) - 1, randint( 1, 5 ) )
	
	id = sessions.addSession( str( randint( 1, 1000000000000000 ) ), "mGoPS" )
	
	for i in us:
		sessions.addUser( id, ut[i] )
		
		fid = foods.addFood( ut[i], menu[randint( 0, len( menu )	 ) - 1], id, ( 0, 0 ) )
		
		sessions.addFood( id, fid )
		
		users.addFood( ut[i], fid )
		

		
		
		
	