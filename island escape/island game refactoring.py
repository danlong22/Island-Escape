import time, winsound, openpyxl, time, pickle

#uses pickle module to load stuff
#prevents me from needing to keep everything in the game file

#pictures
pictures_in = open("island escape pictures.pickle", 'rb')
pictures_dict = pickle.load(pictures_in)

#descriptions
descriptions_in = open("island escape descriptions.pickle", "rb")
descriptions_dict = pickle.load(descriptions_in)


#use to add an item or to change components into a new item
#use blank strings when there are less than 3 components used
#append_item('machete', '', '', 'dull machete'
'''the picture is taken from a dictionary in "island escape pictures.pickle"
so a new entry into that pickle file should be made for each item, or the 
game will crash'''
def new_item(component_1, component_2, component_3, add):
	inventory.append('%s'% add)
	components =[component_1, component_2, component_3]
	for component in components:
		if component in inventory:
			inventory.remove(component)
	#prints picture pulled from dict in 'island escape pictures.pickle'. The key is the
	#name of the item added to the inventory
	print(pictures_dict['%s' % add])

#no clue why, but I have to tell it to print the beach stuff here, otherwise it wont do it
#just by calling the location() method
def death():
	print(pictures_dict['death'])
	input('\nPress any key to restart\n')
	move_to = 'beach'
	print(move_to.center(150, ' ') + '\n')
	print('You are on a lonely stretch of beach. You hear the soft rattle of sand washing to-and fro in the light surf. A small crab skitters about his businees. The ocean stretches to the southern horizon. There is more beach to the West and the East. There is jungle to the North, but you wont be able to penetrate the thick undergrowth without a tool to clear the way.\n')
	location('beach', 'outer jungle', 'stream', 'ocean', 'coconut beach')
	tiger_Dead = False



#credits are in a seperate spreadsheet
def credits():
	print('CREDITS'.center(150,'-'))

	#reads the spreadsheet that the data is recorded on
	wb = openpyxl.load_workbook('credits_spreadsheet.xlsx')
	sheet = wb.active
	for credit in range (1,sheet.max_row):
		for row in range (3):
			print(list(sheet.rows)[0][row].value +': ' + list(sheet.rows)[credit][row].value)
		print('\n')

def commands():
	Actions ={'Move North':'n', 'Move South': 's', 'Move East': 'e', 'Move West': 'w','View Commands': '?', 'View Inventory': 'inventory', 'See Credits': 'credits'}
	print(' '*3 + 'Action'+' '*7 + 'keystroke')
	for k,v in Actions.items():
		print(k + '.'*(20-len(k)) + "'" + v + "'")
	print('\n')

def location (current_location, n, e, s, w, ):
	
	location = current_location 

	#plays a sound file that is named after the location. Saves 1 line per location
	#------------------------------ name the sound files after the location they will be used in-----------------------
	winsound.PlaySound('sounds/%s.wav'% (location), winsound.SND_ASYNC)

	#prints decription of the area. Description is stored in a pickle file
	#---------------------include a description in the pickle file or the game will crash
	print(descriptions_dict['%s' % location])

	#receieves player input
	player_input = input('Type a command or direction: ')

	#handles player commands
	global move_to
	if player_input == 'n':
		if n ==location:
			print('\nYou can\'t go that way.')
			winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)

		else:
			move_to = n
	elif player_input == 'e':
		if e == location:
			print('\nYou can\'t go that way.')
			winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)
		else:
			move_to = e
	elif player_input == 's':
		if s == location:
			print('\nYou can\'t go that way.')
			winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)
		else:
			move_to = s
	elif player_input == 'w':
		if w == location:
			print('\nYou can\'t go that way.')
			winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)
		else:
			move_to = w
	elif player_input == '?':
		commands()
	elif player_input == 'inventory':
		print ('\nINVENTORY: \n')
		for item in inventory:
			print(item)
	elif player_input == 'credits':
		credits()
#begin and explain the game
print('\n')
print(' Welcome to Island Escape '.center(150, '='))
print('\nCongradulations, you have survived a catostrophic place crash/ shipwreck/ alien abduction/ whatever. Unfortunatly you are stuck on this island and need to explore it to find a way off.\n')
print('How To Play:'.center(150,'-') + '\n Island Escape is a text-based adventure game where you move your character North, South, East, and West aroudn the island, searching for items and tools that will help you progress.\n')
commands()

#initialize game
move_to = 'beach'
inventory = []
tiger_dead = False
game_on = True

while game_on == True:

	#coconut beach
	if move_to == 'coconut beach':
		print(move_to.center(150, ' ') + '\n')
		if 'coconut husk' not in inventory:
			print('You pick up one of the fallen coconuts. The husk is stringy and could maybe make some good cord.\n Coconut husk added to inventory.\n')
			new_item('','','', 'coconut husk')

		location('coconut beach', 'coconut beach', 'beach', 'ocean', 'coconut beach')
		
		
	#beach
	if move_to == 'beach':
		print(move_to.center(150, ' ') + '\n')
		location('beach', 'outer jungle', 'stream', 'ocean', 'coconut beach')

	#stream
	if move_to == 'stream':
		winsound.PlaySound('stream.wav', winsound.SND_ASYNC)
		print(move_to.center(150, ' ') + '\n')
		location('stream', 'cave', 'piranah_stream', 'ocean', 'beach')
	#nothing
	#outer jungle
	if move_to == 'outer jungle' and 'machete' in inventory:
		inventory.remove('machete')
		inventory.append('dull machete')
		print('You hack your way through the brambles and vines clogging the ground and enter the jungle. Your already neglected machete is further dulled from use.\n')
	if move_to == 'outer jungle' and 'machete' in inventory or move_to == 'outer jungle' and 'dull machete' in inventory:
		print(move_to.center(150, ' ') + '\n')
		location('outer jungle', 'deep jungle', 'outer jungle', 'beach', 'outer jungle')
	elif move_to == 'outer jungle' and 'machete' not in inventory:
		print('You can\'t get through here without some kind of tool to get through the thick underbrush.\n')
		move_to = 'beach'
	#cave
	if move_to == 'cave':
		print(move_to.center(150, ' ') + '\n')
		if 'machete' not in inventory and 'dull machete' not in inventory:
			print('Your foot hits something, making it slide forward with a metalic clatter. You bend down to pick it up and your hand grasps the handle of a machete. \n machete added to inventory.\n')
			new_item('', '', '', 'machete')
		location ('cave', 'deep cave', 'cave', 'stream', 'cave')
	#bamboo grove
	if move_to == 'bamboo grove':
		print(move_to.center(150, ' ') + '\n')
		if 'coconut husk' and 'spear head' in inventory:
			print('You have an idea. You attach the spear head to the shaft with coconut husk cord and create a respectable weapon. You feel safer already.\n Coconut husk and spear head removed from inventory and spear added.\n')
			new_item('coconut husk', 'spear head', '', 'spear')
		if 'torch' not in inventory:
			print('You cut a short shaft, and smear the sap on the end to create a torch.\n Sap removed from inventory and torch added.\n')
			new_item('sap', '','', 'torch')
		if 'spear' not in inventory:
			print('One of these shafts might be useful for something else, but you are not yet sure what.\n')
		location ('bamboo grove', 'bamboo grove', 'deep jungle', 'bamboo grove', 'bamboo grove')
		
	#deep jungle
	if move_to == 'deep jungle':
		print(move_to.center(150, ' ') + '\n')
		if 'sap' not in inventory and 'torch' not in inventory:
			print('You see a sticky sap leaking from a tree trunk. This could be useful.\n Sap added to inventory\n')
			new_item('', '', '', 'sap')
		location('deep jungle', 'tiger', 'deep jungle', 'outer jungle', 'bamboo grove')
		
	#deep cave
	if move_to == 'deep cave' and 'torch' in inventory:
		print(move_to.center(150, ' ') + '\n')
		print('The light from your torch cuts through the darkness, illuminating a progressivly widening cave.\n')
		if 'spear head' not in inventory:
			print('Your foot catches a protrusion on the floor of the cave, and you stumble, dropping your machete. The machete clatters to the floor, chipping off a peice of rock. You retrieve both and find the rock chip to be razor sharp and conveniently shaped like a spear head.\n Spear head added to inventory.\n')
			new_item('','','', 'spear head')
		location('deep cave', 'deep cave', 'deep cave', 'cave', 'deep cave')
		
	elif move_to == 'deep cave' and 'torch' not in inventory:
		print('You can\'t go that way without a torch.\n')
		location ('cave', 'deep cave', 'cave', 'stream', 'cave')
	#nothing
	#tiger
	if move_to =='tiger' and tiger_dead == False:
		input()
		print('You hear a rustle to your left, you snap your head around and see nothing. You hear another growl and a rustle from your right, but see nothing when you look.\n')
		input()
		if 'spear' in inventory:
			print('You tighten your grip on your spear, square your stance, and get ready to fight for your life.\n')
			input()
		print('You catch a flash of movement from your peripheral vision. Your mind just barely registers a huge feline beast before it is upon you in a frenzy of fur, teeth and claws.\n')
		winsound.PlaySound('sounds//tiger_roar.wav', winsound.SND_ASYNC)
		if 'spear' in inventory:
			print('Time slows down as you level your crude spear at the charging tiger. It leaps, rocketing towards you, claws outstretched.\n')
			input()
			print('Luck and courage guide the tip of the spear on target, and the beast\'s momentum drives the spear through it\'s heart. You both fall to the ground. You just barely scramble away from it\'s flailing claws as it screeches in fury and agony. It convulses a few times, then lets out it\'s final breath. So much for the endagered species list...\n')
			tiger_dead = True
			winsound.PlaySound('sounds//tiger dies.wav', winsound.SND_FILENAME)
			print('You step over the tiger\'s dead carcass as you continue on your way. The jungle to the East and West is impassable, there is passable jungle to the South, and there are climbable cliffs to the North.\n')	
		else:
			print('Your thin skin and soft nails are no match for the tiger\'s rending claws. Your flesh is peeled off your bones in sheets like skin from an orange. You sqeeze your eyes shut and beg for the release of Death.\n')
			winsound.PlaySound('sounds//scream.wav', winsound.SND_ASYNC)
			death()
	if move_to == 'tiger' and tiger_dead == True:
		print(move_to.center(150, ' ') + '\n')
		print('You step over the tiger\'s dead carcass as you continue on your way. The jungle to the East and West is impassable, there is passable jungle to the South, and there are climbable cliffs to the North.\n')	
		location('tiger', 'cliffs', 'tiger', 'deep jungle', 'tiger')

	#nothing
	#cliffs
	if move_to =='cliffs':
		print(move_to.center(150, ' ') + '\n')
		print('You\'ve reached the cliffs. To be continued...')
		input()
		break
	#ocean
	if move_to == 'ocean':
		
		print('You dive in, and start swimming in the direction you belive home to be. The current is deceptivly strong, and by the time you realize you\'ve underestimated the ocean, it is too late to swim back.')
		input()
		print('The current pulls you under, and drags your body across jagged coral. You try to scream, but inhale a mouthful of seawater and begin to panic. You claw your way towards the surface, but are again swept to the bottom by the waves...\n')
		input()
		winsound.PlaySound('sounds//ocean.wav', winsound.SND_ASYNC)
		print('it\'s not so bad down here...\n')
		input()
		print('You feel warm and peacful...\n')
		input()
		print('you close your eyes and embrace the darkness.\n')
		death()
	if move_to == 'piranah_stream':
		winsound.PlaySound('sounds//stream.wav', winsound.SND_ASYNC)
		print('\nYou\'re a strong swimmer and decide to explore the opposite shore. You get about halfway accross when you feel a sharp pain on your arm. Before you can investigate, you feel more of the same. In a moment of sickening clarity, you realize that you are in piranah infested water.')
		input()
		print('You swim hard for the opposite shore, as the carnivorous fish tear your flesh from your body bit by tiny bit.')
		input()
		print('in excurutiating pain, you see the opposite shore getting closer and closer. You realize that you can make it and swim harder, willing away the agony of being eaten alive.')
		input()
		print('You\'d failed to notice the floating log that had been getting closer and closer this entire time. Far too late, you realize that it is a massive reptile. Your leg explodes in pain as a vice-like grip takes your leg, and drags you down.')
		input()
		winsound.PlaySound('sounds//scream.wav', winsound.SND_ASYNC)
		death()





