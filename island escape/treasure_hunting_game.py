import random

'''beach = [['','','','',''],
		 ['','','','',''],
		 ['','','','',''],
		 ['','','','',''],
		 ['','','','','']
]'''
player_lattitude = 2
player_longitude = 2


#treasure location
treasure_lattitude = random.randint(0,4)
treasuer_longitude = random.randint(0,4)

print(treasure_location[0])
#distance from treasure
'''if ((player_location[0]) - (treasure_location[0])) < ((player_location[1]) - (treasure_location[1])):
	distance = player_location[0] - treasure[0]
elif player_location[1] - treasure[1] < player_location[0] - treasure_location[0]:
	distance = player_location[1] - treasure[1]
else:
	distance = player_location[1] - treasure[1]'''