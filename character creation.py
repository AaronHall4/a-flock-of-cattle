def dwarf():
	asi=[0,0,2,0,0,0]
	subType=str(input('Would you like to be a Hill Dwarf or a Mountain Dwarf? (Hill or Mountain)'))
	while subType.lower() not in 'hill mountain':
		subType=str(input('Would you like to be a Hill Dwarf or a Mountain Dwarf? (Hill or Mountain)'))
	if subType.lower()=='hill':
		asi[3]=1
		dwarvenToughness=True
		dwarvenArmorTraining=False
	else:
		asi[0]=2
		dwarvenToughness=False
		dwarvenArmorTraining=True
	asi[7]=dwarvenToughness
	asi[8]=dwarvenArmorTraining
	asi[6]=subType
	return asi

def elf():
	asi=[0,2,0,0,0,0,30]
	subType=str(input('Would you like to be a High Elf, Wood Elf, or Dark Elf (Drow)? (High, Wood or Drow)'))
	while subType.lower() not in 'high wood drow':
		subType=str(input('ould you like to be a High Elf, Wood Elf, or Dark Elf (Drow)? (High, Wood or Drow)'))
	if subType.lower()=='high':
		asi[4]=1
		elfWeaponTraining=True
		cantrip=True
		extraLanguage=True
		maskOfTheWild=False
		superiorDarkvision=False
		drowMagic=False
		drowWeaponTraining=False
	elif subType.lower()=='wood':
		asi[2]=1
		elfWeaponTraining=True
		cantrip=False
		extraLanguage=False
		asi[6]=35
		maskOfTheWild=True
		superiorDarkvision=False
		drowMagic=False
		drowWeaponTraining=False
	else:
		asi[5]=1
		superiorDarkvision=True
		sunlightSensitivity=True
		drowMagic=True
		drowWeaponTraining=True
		elfWeaponTraining=False
		cantrip=False
		extraLanguage=False
		maskOfTheWild=False
	asi[8]=elfWeaponTraining
	asi[9]=cantrip
	asi[10]=extraLanguage
	asi[11]=maskOfTheWild
	asi[12]=superiorDarkvision
	asi[13]=drowMagic
	asi[14]=drowWeaponTraining
	asi[15]=sunlightSensitivity
	asi[7]=subType
	return asi

def halfling():
	asi=[0,2,0,0,0,0]
	subType=str(input('Would you like to be a Lightfoot Halfling or a Stout Halfling? (Lightfoot or Stout)'))
	while subType.lower() not in 'lightfoot stout':
		subType=str(input('Would you like to be a Lightfoot Halfling or a Stout Halfling? (Lightfoot or Stout)'))
	if subType.lower()=='lightfoot':
		asi[5]=1
		naturallyStealthy=True
		stoutResilience=False
	else:
		asi[2]=1
		naturallyStealthy=False
		stoutResilience=True
	asi[7]=naturallyStealthy
	asi[8]=stoutResilience
	asi[6]=subType
	return asi

def dragonborn():
	asi=[2,0,0,0,0,1]
	ancestries=['black', 'blue', 'brass', 'bronze', 'copper', 'gold', 'green', 'red', 'silver', 'white']
	ancestry=str(input('Would you like to be a black, blue, brass, bronze, copper, gold, green, red, silver, or white dragonborn? (input the color) '))
	while ancestry.lower() not in ancestries:
		ancestry=str(input('Would you like to be a black, blue, brass, bronze, copper, gold, green, red, silver, or white dragonborn? (input the color) '))
	if ancestry=='black' or ancestry=='copper':
		damageType='Acid'
	elif ancestry=='blue' or ancestry=='bronze':
		damageType='Lightning'
	elif ancestry=='brass' or ancestry=='gold' or ancestry=='red':
		damageType='Fire'
	elif ancestry=='silver' or ancestry=='white':
		damageType='Cold'
	else:
		damageType='Poison'
	asi[6]=damageType
	asi[7]=ancestry
def gnome():
	asi=[0,0,0,0,2,0]
	subType=str(input('Would you like to be a Forest Gnome or a Rock Gnome? (Forest or Rock)'))
	while subType.lower() not in 'forest rock':
		subType=str(input('Would you like to be a Forest Gnome or a Rock Gnome? (Forest or Rock)'))
	if subType.lower()=='forest':
		asi[1]=1
		naturalIllusionist=True
		speakWithSmallBeasts=True
		artificersLore=False
		tinker=False
	else:
		asi[2]=1
		naturalIllusionist=False
		speakWithSmallBeasts=False
		artificersLore=True
		tinker=True
	asi[7]=naturalIllusionist
	asi[8]=speakWithSmallBeasts
	asi[9]=artificersLore
	asi[10]=tinker
	asi[6]=subType

def halfelf():
	asi=[0,0,0,0,0,2]
	asiOne=str(input('Which ability score would you like to increase by 1? (Strength, Dexterity, Constitution, Wisdom or Intelligence)'))
	while asiOne.lower() not in 'strength dexterity constitution wisdom intelligence':
		asiOne=str(input('Which ability score would you like to increase by 1? (Strength, Dexterity, Constitution, Wisdom or Intelligence)'))
	asiTwo=str(input('Which ability score would you like to increase by 1? (Pick a different one)'))
	while asiTwo.lower() not in 'strength dexterity constitution wisdom intelligence' or asiTwo==asiOne:
		asiTwo=str(input('Which ability score would you like to increase by 1? (Pick a different one)'))
	asiOne=asiOne.lower()
	asiTwo=asiTwo.lower()
	if asiOne=='strength' or asiTwo=='strength':
		asi[0]=1
	if asiOne=='dexterity' or asiTwo=='dexterity':
		asi[1]=1
	if asiOne=='constitution' or asiTwo=='constitution':
		asi[2]=1
	if asiOne=='wisdom' or asiTwo=='wisdom':
		asi[3]=1
	if asiOne=='intelligence' or asiTwo=='intelligence':
		asi[4]=1
	skillOne=str(input('Choose a skill to gain proficiency in: '))
	skillTwo=str(input('Choose another skill to gain proficiency in: '))
	while skillTwo==skillOne:
		skillTwo=str(input('Choose a different skill to gain proficiency in: '))
	language=str(input('Choose an extra language to know: '))
	asi[6]=skillOne
	asi[7]=skillTwo
	asi[8]=language


def characterCreation(recRace, recClass):
	raceList=['dwarf', 'elf', 'halfling', 'human', 'dragonborn', 'gnome', 'half-elf', 'half-orc', 'tiefling']
	classList=['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
	userRace=str(input('Would you like to be a',recRace,'or would you like to choose another race? (Yes/Other) '))
	if userRace.lower()=='yes':
		userRace=recRace
	elif userRace.lower()=='other':
		userRace=str(input('Would you like to be a dwarf, elf, halfling, human, dragonborn, gnome, half-elf, half-orc, or tiefling? '))
		userRace=userRace.lower()
		while userRace not in raceList:
			userRace=str(input('Would you like to be a dwarf, elf, halfling, human, dragonborn, gnome, half-elf, half-orc, or tiefling? '))
			userRace=userRace.lower()
	else:
		while userRace not in raceList:
			userRace=str(input('Would you like to be a',recRace,'or would you like to choose another race? (Yes/Other) '))
			if userRace.lower()=='yes':
				userRace=recRace
			elif userRace.lower()=='other':
				userRace=str(input('Would you like to be a dwarf, elf, halfling, human, dragonborn, gnome, half-elf, half-orc, or tiefling? '))
				userRace=userRace.lower()
	userClass=str(input('Would you like to be a',recClass,'or would you like to choose another race? (Yes/Other) '))
	if userClass.lower()=='yes':
		userClass=recClass
	elif userClass.lower()=='other':
		userClass=str(input('Would you like to be a barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, or wizard? '))
		userClass=userClass.lower()
		while userClass not in classList:
			userClass=str(input('Would you like to be a barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, or wizard? '))
			userClass=userClass.lower()
	else:
		while userClass not in classList:
			userClass=str(input('Would you like to be a',recClass,'or would you like to choose another class? (Yes/Other) '))
			if userClass.lower()=='yes':
				userClass=recClass
			elif userClass.lower()=='other':
				userClass=str(input('Would you like to be a barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, or wizard? '))
				userClass=userClass.lower()
	proficiences=[]
	attributes=[]
	languages=[]
	cantrips=[]
	hpMax=0
	if userRace=='dwarf':
		results=dwarf()
		asi=results[0:6]
		subType=results[6]
		if results[7]:
			hpMax=1
		if results[8]:
			proficiences+=['light armor','medium armor']
		walkingSpeed=25
		tools=['smith','brewer','mason']
		toolProficiency=str(input('Would you like proficiency in smith\'s tools, brewer\'s tools, or artisans\'s tools '))
		while toolProficiency.lower() not in tools:
			toolProficiency=str(input('Would you like proficiency in smith\'s tools, brewer\'s tools, or artisans\' tools '))
		proficiences+=[toolProficiency.lower(),'battleaxe','handaxe','throwing hammer','warhammer']
		attributes+=['darkvision','Dwarven Resilience','Stonecunning']
		languages+=['Common','Dwarvish']
	elif userRace=='elf':
		results=elf()
		asi=results[0:6]
		subType=results[6]
		walkingSpeed=results[7]
		if results[8]:
			proficiences+=['longsword','shortsword','shortbow','longbow']
		if results[9]:
			cantrips+=[str(input('Pick a wizard cantrip to know: '))]
		if results[10]:
			languages+=[str(input('Pick an extra language to know: '))]
		if results[11]:
			attributes+=['Mask of the Wild']
		if results[12]:
			attributes+=['Superior Darkvision']
		else:
			attributes+=['Darkvision']
		if results[13]:
			cantrips+=['Dancing Lights']
		if results[14]:
			proficiences+=['rapier','shortsword','hand crossbow']
		if results[15]:
			attributes+=['Sunlight Sensitivity']
		attributes+=['Keen Senses','Fey Ancestry','Trance']
		languages+=['Common','Elvish']
	elif userRace=='halfling':
		results=halfling()
		asi=results[0:6]
		subType=results[6]
		if results[7]:
			attributes+=['Naturally Stealthy']
		if results[8]:
			attributes+=['Stout Resilience']
		walkingSpeed=25
		attributes+=['Lucky','Brave','Halfling Nimbleness']
		languages+=['Common','Halfling']
	elif userRace=='human':
		asi=[1,1,1,1,1,1]
		walkingSpeed=30
		language=str(input('Select an extra language to know: '))
		languages+=['Common',language]
	elif userRace=='dragonborn':
		results=dragonborn()
		asi=results[0:6]
		damageType=results[6]
		subType=results[7]
		walkingSpeed=30
		attributes+=['Breath Weapon: '+damageType, 'Damage Resistance: '+damageType]
		languages+=['Common','Draconic']
	elif userRace=='gnome':
		results=gnome()
		asi=results[0:6]
		if results[7]:
			cantrips+=['Minor Illusion']
		if results[8]:
			attributes+=['Speak with Small Beasts']
		if results[9]:
			attributes+=['Artificer\'s Lore']
		if results[10]:
			attributes+=['Tinker']
		subType=results[6]
	elif userRace=='half-elf':
		results=halfelf()
		asi=results[0:6]
		proficiences+=results[6:8]
		languages+=results[8]
		languages+=['Common','Elvish']
		attributes+=['Darkvision','Fey Ancestry']
		walkingSpeed=30
	elif userRace=='half-orc':
		asi=[2,0,1,0,0,0]
		walkingSpeed=30
		attributes+=['Darkvision','Relentless Endurance','Savage Attacks']
		proficiences+=['Intimidation']
		languages+=['Common','Orc']
	else:
		asi=[0,0,0,0,1,2]
		walkingSpeed=30
		attributes+=['Darkvision','Hellish Resistance']
		cantrips+=['thaumaturgy']
		languages+=['Common','Infernal']


