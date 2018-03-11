import random

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
	equipment=[]
	if userClass=='barbarian':
		hitDice=12
		hpMax+=12
		if subType!='mountain':
			proficiences+=['light armor','medium armor']
		proficiences+=['shields','simple weapons','martial weapons']
		savingThrows=[0,2]
		skillOne=str(input('Choose one of the following: Animal Handling, Intimidation, Nature, Perception, and Survival '))
		skillTwo=str(input('Choose another one of those skills'))
		while skillOne.lower()==skillTwo.lower():
			skillTwo=str(input('Choose a different one of those skills'))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=input('Would you like a greataxe or any martial melee weapon?')
		if equipmentChoice==1:
			equipment+=['greataxe']
		else:
			equipment+=['any martial melee weapon']
		equipmentChoice=input('Would you like two handaxes or any simple weapon?')
		if equipmentChoice==1:
			equipment+=['2 handaxes']
		else:
			equipment+=['any simple weapon']
		equipment+=['explorer\'s pack','four javelins']
		attributes+=['2 rages','unarmored defense']
	if userClass=='bard':
		hitDice=8
		hpMax+=8
		if 'light armor' not in proficiences:
			proficiences+=['light armor']
		proficiences+='simple weapons'
		if 'hand crossbow' not in proficiences:
			proficiences+=['hand crossbow']
		if 'longsword' not in proficiences:
			proficiences+=['longsword']
		if 'rapier' not in proficiences:
			proficiences+=['rapier']
		if 'shortsword' not in proficiences:
			proficiences+=['shortsword']
		savingThrows=[1,5]
		proficiences+=[str(input('Choose a musical instrument to become proficient in:'))]
		proficiences+=[str(input('Choose another musical instrument to become proficient in:'))]
		proficiences+=[str(input('Choose a third musical instrument to become proficient in:'))]
		skillOne=str(input('Choose a skill you\'re not already proficient in: '))
		skillTwo=str(input('Choose a different skill you\'re not already proficient in: '))
		skillThree=str(input('Choose a third skill you\'re not already proficient in '))
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 to choose the third if there is one.')
		equipmentChoice=input('Would you like a rapier, a longsword, or any simple weapon?')
		if equipmentChoice==1:
			equipment+=['rapier']
		elif equipmentChoice==2:
			equipment+=['longsword']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=input('Would you like a diplomat\'s pack or and entertainer\'s pack?')
		if equipmentChoice==1:
			equipment+=['diplomat\'s pack']
		else:
			equipment+=['entertainer\'s pack']
		equipmentChoice=input('Would you like a lute or another musical instrument?')
		if equipmentChoice==1:
			equipment+=['lute']
		else:
			equipment+=['any musical instrument']
		equipment+=['leather armor','dagger']
	if userClass=='cleric':
		hitDice=8
		hpMax+=8
		if 'light armor' not in proficiences:
			proficiences+=['light armor']
		if 'medium armor' not in proficiences:
			proficiences+=['medium armor']
		proficiences+=['shields']
		proficiences+=['all simple weapons']
		savingThrows=[3,5]
		skillOne=str(input('Choose a skill: History, Insight, Medicine, Persuasion, or Religion '))
		skillTwo=str(input('Choose another skill from above:'))
		while skillTwo.lower()==skillOne.lower():
			skillTwo=str(input('Choose another skill from above:'))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=input('Would you like a Mace or a Warhammer (choose warhammer only if you\'re a Dwarf) ')
		if equipmentChoice==1:
			equipment+=['mace']
		else:
			equipment+=['warhammer']
		equipmentChoice=input('Would you like scale mail or leather armor?')
		if equipmentChoice==1:
			equipment+=['scale mail']
		else:
			equipment+=['leather armor']
		equipmentChoice=input('Would you like a light crossbow and 20 bolts or any simple weapon? ')
		if equipmentChoice==1:
			equipment+=['light crossbow and 20 bolts']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=input('Would you like a priest\'s pack or an explorer\'s pack? ')
		if equipmentChoice==1:
			equipment+=['priest\'s pack']
		else:
			equipment+=['explorer\'s pack']
		equipment+=['shield','holy symbol']
	if userClass=='druid':
		hitDice=8
		hpMax+=8
		if 'light armor' not in proficiences:
			proficiences+=['light armor']
		if 'medium armor' not in proficiences:
			proficiences+=['medium armor']
		proficiences+=['shield','club','dagger','dart','javelin','mace','quarterstaff','scimitar','sickle','sling','spear','herbalism kit']
		savingThrows=[3,4]
		skillOne=str(input('Choose a skill from the following: Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival'))
		skillTwo=str(input('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=input('Would you like a wooden shield or any simple weapon? ')
		if equipmentChoice==1:
			equipment+=['wooden shield']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=input('Would you like a scimitar or any simple melee weapon?')
		if equipmentChoice==1:
			equipment+=['scimitar']
		else:
			equipment+=['any simple melee weapon']
		equipment+=['leather armor','explorer\'s pack', 'druidic focus']
	if userClass=='fighter':
		hitDice=10
		hpMax+=10
		proficiences+=['armor','shields','simple weapons','martial weapons']
		savingThrows=[0,2]
		skillOne=str(input('Choose a skill from the following: Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, or Survival'))
		skillTwo=str(input('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=input('Would you like chain mail or leather armor, a longbow, and 20 arrows? ')
		if equipmentChoice==1:
			equipment+=['chain mail']
		else:
			equipment+=['leather armor','longbow','twenty arrows']
		equipmentChoice=input('Would you like a martial weapon and a shield or 2 martial weapons?')
		if equipmentChoice==1:
			equipment+=['martial weapons','shield']
		else:
			equipment+=['two martial weapons']
		equipmentChoice=input('Would you like a light crossbow and 20 bolts or two handaxes? ')
		if equipmentChoice==1:
			equipment+=['light crossbow', '20 bolts']
		else:
			equipment+=['two handaxes']
		equipmentChoice=input('Would you like a dungeoneer\'s pack or an explorer\'s pack? ')
		if equipmentChoice==1:
			equipment+=['dungeoneer\'s pack']
		else:
			equipment+=['explorer\'s pack']
	if userClass=='monk':
		hitDice=8
		hpMax+=8
		proficiences+=['simple weapons']
		if 'shortsword' not in proficiences:
			proficiences+=['shortsword']
		proficiences+=[str(input('Choose a type of artisan\'s tools or a musical instrument to be proficient with: '))]
		savingThrows=[0,1]
		skillOne=str(input('Choose a skill from the following: Acrobatics, Athletics, History, Insight, Religion, or Stealth'))
		skillTwo=str(input('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=input('Would you like a shortsword or any simple weapon? ')
		if equipmentChoice==1:
			equipment+=['shortsword']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=input('Would you like a dungeoneer\'s pack or an explorer\'s pack? ')
		if equipmentChoice==1:
			equipment+=['dungeoneer\'s pack']
		else:
			equipment+=['explorer\'s pack']
		equipment+=['10 darts']
	if userClass=='paladin':
		hitDice=10
		hpMax+=10
		proficiences+=['armor','shields','simple weapons','martial weapons']
		savingThrows=[3,5]
		skillOne=str(input('Choose a skill from the following: Atheltics, Insight, Intimidation, Medicine, Persuasion, or Religion'))
		skillTwo=str(input('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=input('Would you like a martial weapon and a shield or 2 martial weapons?')
		if equipmentChoice==1:
			equipment+=['martial weapons','shield']
		else:
			equipment+=['two martial weapons']
		equipmentChoice=input('Would you like five javelins or any simple melee weapon? ')
		if equipmentChoice==1:
			equipment+=['light crossbow', '20 bolts']
		else:
			equipment+=['two handaxes']
		equipmentChoice=input('Would you like a priest\'s pack or an explorer\'s pack? ')
		if equipmentChoice==1:
			equipment+=['priest\'s pack']
		else:
			equipment+=['explorer\'s pack']
		equipment+=['chain mail','holy symbol']
	if userClass=='ranger':
		hitDice=10
		hpMax+=10
		if 'light armor' not in proficiences:
			proficiences+=['light armor']
		if 'medium armor' not in proficiences:
			proficiences+=['medium armor']
		proficiences+=['shields']
		savingThrows=[0,1]
		skillOne=str(input('Choose a skill from the following: Animal Handling, Atheltics, Insight, Investigation, Nature, Perception, Stealth, or Survival'))
		skillTwo=str(input('Choose a different skill from the above: '))
		skillThree=str(input('Choose a third skill from the above: '))
		proficiences+=[skillOne,skillTwo,skillThree]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=input('Would you like scale mail or leather armor?')
		if equipmentChoice==1:
			equipment+=['scale mail']
		else:
			equipment+=['leather armor']
		equipmentChoice=input('Would you like two shortswords or two simple melee weapons? ')
		if equipmentChoice==1:
			equipment+=['two shortswords']
		else:
			equipment+=['two simple melee weapons']
		equipmentChoice=input('Would you like a dungeoneer\'s pack or an explorer\'s pack? ')
		if equipmentChoice==1:
			equipment+=['dungeoneer\'s pack']
		else:
			equipment+=['explorer\'s pack']
		equipment+=['longbow','quiver of 20 arrows']
	if userClass=='rogue':
		hitDice=8
		hpMax+=8
		if 'light armor' not in proficiences:
			proficiences+=['light armor']
		proficiences+=['simple weapons']
		if 'hand crossbow' not in proficiences:
			proficiences+=['hand crossbow']
		if 'longsword' not in proficiences:
			proficiences+=['longsword']
		if 'rapier' not in proficiences:
			proficiences+=['rapier']
		if 'shortsword' not in proficiences:
			proficiences+=['shortsword']
		proficiences+=['thieves\' tools']
		savingThrows=[1,4]
		skillOne=str(input('Choose a skill from the following: Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, or Stealth'))
		skillTwo=str(input('Choose a different skill from the above: '))
		skillThree=str(input('Choose a third skill from the above: '))
		skillFour=str(input('Choose a fourth skill from the above: '))
		proficiences+=[skillOne,skillTwo,skillThree,skillFour]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=input('Would you like a rapier or a shortsword?')
		if equipmentChoice==1:
			equipment+=['rapier']
		else:
			equipment+=['shortsword']
		equipmentChoice=input('Would you like a shortbow and 20 arrows or a shortsword? ')
		if equipmentChoice==1:
			equipment+=['shortbow', '20 arrows']
		else:
			equipment+=['shortsword']
		equipmentChoice=input('Would you like a burglar\'s pack, a dungeoneer\'s pack, or an explorer\'s pack? ')
		if equipmentChoice==1:
			equipment+=['burglar\'s pack']
		elif equipmentChoice==2:
			equipment+=['dungeoneer\'s pack']
		else:
			equipment+=['explorer\'s pack']
		equipment+=['leather armor','two daggers','thieves\' tools']
	if userClass=='sorcerer':
		hitDice=6
		hpMax+=6
		proficiences+=['dagger','dart','sling','quarterstaff','light crossbow']
		savingThrows=[2,5]
		skillOne=str(input('Choose a skill from the following: Arcana, Deception, Insight, Intimidation, Persuasion, or Religion'))
		skillTwo=str(input('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=input('Would you like a light crossbow and 20 bolts or any simple weapon')
		if equipmentChoice==1:
			equipment+=['light crossbow','20 bolts']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=input('Would you like a component pouch or an arcane focus? ')
		if equipmentChoice==1:
			equipment+=['component pouch']
		else:
			equipment+=['arcane focus']
		equipmentChoice=input('Would you like a dungeoneer\'s pack, or an explorer\'s pack? ')
		if equipmentChoice==1:
			equipment+=['dungeoneer\'s pack']
		else:
			equipment+=['explorer\'s pack']
		equipment+=['two daggers']
	if userClass=='warlock':
		hitDice=8
		hpMax+=8
		if 'light armor' not in proficiences:
			proficiences+=['light armor']
		proficiences+=['simple weapons']
		savingThrows=[3,5]
		skillOne=str(input('Choose a skill from the following: Arcana, Deception, History, Intimidation, Investigation, History, or Religion'))
		skillTwo=str(input('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=input('Would you like a light crossbow and 20 bolts or any simple weapon')
		if equipmentChoice==1:
			equipment+=['light crossbow','20 bolts']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=input('Would you like a component pouch or an arcane focus? ')
		if equipmentChoice==1:
			equipment+=['component pouch']
		else:
			equipment+=['arcane focus']
		equipmentChoice=input('Would you like a dungeoneer\'s pack, or a scholar\'s pack? ')
		if equipmentChoice==1:
			equipment+=['dungeoneer\'s pack']
		else:
			equipment+=['scholar\'s pack']
		equipment+=['leather armor','any simple weapon','two daggers']
	if userClass=='wizard':
		hitDice=6
		hpMax+=6
		proficiences+=['dagger','dart','sling','quarterstaff','light crossbow']
		savingThrows=[3,4]
		skillOne=str(input('Choose a skill from the following: Arcana, History, Insight, Investigation, Medicine, or Religion'))
		skillTwo=str(input('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=input('Would you like a quarterstaff or a dagger')
		if equipmentChoice==1:
			equipment+=['quarterstaff']
		else:
			equipment+=['dagger']
		equipmentChoice=input('Would you like a component pouch or an arcane focus? ')
		if equipmentChoice==1:
			equipment+=['component pouch']
		else:
			equipment+=['arcane focus']
		equipmentChoice=input('Would you like a explorer\'s pack, or a scholar\'s pack? ')
		if equipmentChoice==1:
			equipment+=['explorer\'s pack']
		else:
			equipment+=['scholar\'s pack']
		equipment+=['a spellbook']