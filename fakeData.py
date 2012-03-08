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


numSessions = 100

menu = restaurant.getMenu( "mGoPS" )

us = users.collection.find()
ut = []
for u in us:
	ut.append( u['uid'] )
for sess in range( numSessions ):
	us = random_integers( 1, len( ut ) - 1, randint( 1, 5 ) )
	
	id = sessions.addSession( str( randint( 1, 1000000000000000 ) ), "mGoPS" )
	
	sessions.setTaxRate( id, 0.06 )
	sessions.setTip( id, 0.2 )
	sessions.addPaymentType( id, "cc" )
	
	menu = foods.getFoodRestaurantMenu( "mGoPS" )
	
	total = 0.0
	
	for i in us:
		sessions.addUser( id, ut[i] )
		ii = menu[ randint( 0, len( menu ) - 1 ) ]
		f = foods.getFoodById( ii['_id'] )
		
		total += f['cost']
		
		sessions.addFood( id, f['_id'] )
		
		users.addFood( ut[i], f['_id'] )
		
	
	sessions.setTotal( id, total )
		
		
	