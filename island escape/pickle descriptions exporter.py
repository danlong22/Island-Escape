import pickle


descriptions_dict = {
	'coconut beach':'You arrive onto another lonely section of beach. There is a scrawny-looking coconut tree giving a little bit of shade. The ocean stretches to the southern horizon. The North and West are blocked by cliffs. There is another section of beach to the East\n.',
	'beach':'You are on a lonely stretch of beach. You hear the soft rattle of sand washing to-and fro in the light surf. A small crab skitters about his businees. The ocean stretches to the southern horizon. There is more beach to the West and the East. There is jungle to the North, but you wont be able to penetrate the thick undergrowth without a tool to clear the way.\n',
	'stream':'A stream empties into the ocean. There is more life here, and you hear various buzzes, calls, and croaks. Some kind of fish are swimming in the water to the East. The oceans stretches to the southern horizon, another section of beach lies to the West, and there is a cave to the North.\n',
	'cave':'This cave is dry and safe, but dark. The light pouring in from the entrance makes your immediate surroundings just barley visible. It continues straight ahead to the north into the pitch black. You will need a light source to continue ahead.\n',
	'outer jungle':'The jungle is full of movement and sound. It is much cooler now that you are out of the sun. There are impassable cliffs to the West and East, more jungle to the North, and a beach to the South.\n',
	'deep cave':'You reach the end of the cave. The mouth you came in through lies to your south.\n',
	'bamboo grove':'There is a grove of sturdy bamboo. The wind rustles their leaves, and rubs their shafts together with an eerie squeeking.\n',
	'deep jungle':'The undegrowth clears a little bit as you penetrate deeper into the jungle. The canopy of the trees blocks almost all sunlight, creating a mid-day twilight. An unscalable cliff rises from the ground to the East. A musty, earthy smell comes from the West. A relativly thick section of jungle lies to the south. As you look to the North, you are struck with an overwhelming sense of unease. Your gut instinct screams DANGER.\n',
	'tiger':'You ignore your sense of unease and proceed North...\n'
}
pickle_out = open("c://users//daniel//desktop//island escape//island escape descriptions.pickle", 'wb')

pickle.dump(descriptions_dict, pickle_out)
pickle_out.close()

