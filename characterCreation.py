import random
from prettyprinters import query
from fdfgen import forge_fdf
import os
from math import floor

def dwarf():
	asi=[0,0,2,0,0,0]
	subType=str(query('Would you like to be a Hill Dwarf or a Mountain Dwarf? (Hill or Mountain)'))
	while subType.lower() not in 'hill mountain':
		subType=str(query('Would you like to be a Hill Dwarf or a Mountain Dwarf? (Hill or Mountain)'))
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
	subType=str(query('Would you like to be a High Elf, Wood Elf, or Dark Elf (Drow)? (High, Wood or Drow)'))
	while subType.lower() not in 'high wood drow':
		subType=str(query('Would you like to be a High Elf, Wood Elf, or Dark Elf (Drow)? (High, Wood or Drow)'))
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
	subType=str(query('Would you like to be a Lightfoot Halfling or a Stout Halfling? (Lightfoot or Stout)'))
	while subType.lower() not in 'lightfoot stout':
		subType=str(query('Would you like to be a Lightfoot Halfling or a Stout Halfling? (Lightfoot or Stout)'))
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
	ancestry=str(query('Would you like to be a black, blue, brass, bronze, copper, gold, green, red, silver, or white dragonborn? (query the color) '))
	while ancestry.lower() not in ancestries:
		ancestry=str(query('Would you like to be a black, blue, brass, bronze, copper, gold, green, red, silver, or white dragonborn? (query the color) '))
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
	return asi

def gnome():
	asi=[0,0,0,0,2,0]
	subType=str(query('Would you like to be a Forest Gnome or a Rock Gnome? (Forest or Rock)'))
	while subType.lower() not in 'forest rock':
		subType=str(query('Would you like to be a Forest Gnome or a Rock Gnome? (Forest or Rock)'))
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
	return asi

def halfelf():
	asi=[0,0,0,0,0,2]
	asiOne=str(query('Which ability score would you like to increase by 1? (Strength, Dexterity, Constitution, Wisdom or Intelligence)'))
	while asiOne.lower() not in 'strength dexterity constitution wisdom intelligence':
		asiOne=str(query('Which ability score would you like to increase by 1? (Strength, Dexterity, Constitution, Wisdom or Intelligence)'))
	asiTwo=str(query('Which ability score would you like to increase by 1? (Pick a different one)'))
	while asiTwo.lower() not in 'strength dexterity constitution wisdom intelligence' or asiTwo==asiOne:
		asiTwo=str(query('Which ability score would you like to increase by 1? (Pick a different one)'))
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
	skillOne=str(query('Choose a skill to gain proficiency in: '))
	skillTwo=str(query('Choose another skill to gain proficiency in: '))
	while skillTwo==skillOne:
		skillTwo=str(query('Choose a different skill to gain proficiency in: '))
	language=str(query('Choose an extra language to know: '))
	asi[6]=skillOne
	asi[7]=skillTwo
	asi[8]=language
	return asi

def characterCreation(recRace, recClass,backstory):
	raceList=['dwarf', 'elf', 'halfling', 'human', 'dragonborn', 'gnome', 'half-elf', 'half-orc', 'tiefling']
	classList=['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
	userRace=str(query('Would you like to be a '+recRace+' or would you like to choose another race? (Yes/Other) '))
	if userRace.lower()=='yes':
		userRace=recRace
	elif userRace.lower()=='other':
		userRace=str(query('Would you like to be a dwarf, elf, halfling, human, dragonborn, gnome, half-elf, half-orc, or tiefling? '))
		userRace=userRace.lower()
		while userRace not in raceList:
			userRace=str(query('Would you like to be a dwarf, elf, halfling, human, dragonborn, gnome, half-elf, half-orc, or tiefling? '))
			userRace=userRace.lower()
	else:
		while userRace not in raceList:
			userRace=str(query('Would you like to be a '+recRace+' or would you like to choose another race? (Yes/Other) '))
			if userRace.lower()=='yes':
				userRace=recRace
			elif userRace.lower()=='other':
				userRace=str(query('Would you like to be a dwarf, elf, halfling, human, dragonborn, gnome, half-elf, half-orc, or tiefling? '))
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
		toolProficiency=str(query('Would you like proficiency in smith\'s tools, brewer\'s tools, or artisans\'s tools '))
		while toolProficiency.lower() not in tools:
			toolProficiency=str(query('Would you like proficiency in smith\'s tools, brewer\'s tools, or artisans\' tools '))
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
			cantrips+=[str(query('Pick a wizard cantrip to know: '))]
		if results[10]:
			languages+=[str(query('Pick an extra language to know: '))]
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
		language=str(query('Select an extra language to know: '))
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
	userClass=str(query('Would you like to be a '+recClass+' or would you like to choose another race? (Yes/Other) '))
	if userClass.lower()=='yes':
		userClass=recClass
	elif userClass.lower()=='other':
		userClass=str(query('Would you like to be a barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, or wizard? '))
		userClass=userClass.lower()
		while userClass not in classList:
			userClass=str(query('Would you like to be a barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, or wizard? '))
			userClass=userClass.lower()
	else:
		while userClass not in classList:
			userClass=str(query('Would you like to be a '+recClass+' or would you like to choose another class? (Yes/Other) '))
			if userClass.lower()=='yes':
				userClass=recClass
			elif userClass.lower()=='other':
				userClass=str(query('Would you like to be a barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, or wizard? '))
				userClass=userClass.lower()
	equipment=[]
	if userClass=='barbarian':
		hitDice=12
		hpMax+=12
		if subType!='mountain':
			proficiences+=['light armor','medium armor']
		proficiences+=['shields','simple weapons','martial weapons']
		savingThrows=[0,2]
		skillOne=str(query('Choose one of the following: Animal Handling, Intimidation, Nature, Perception, and Survival '))
		skillTwo=str(query('Choose another one of those skills'))
		while skillOne.lower()==skillTwo.lower():
			skillTwo=str(query('Choose a different one of those skills'))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=query('Would you like a greataxe or any martial melee weapon?')
		if equipmentChoice==1:
			equipment+=['greataxe']
		else:
			equipment+=['any martial melee weapon']
		equipmentChoice=query('Would you like two handaxes or any simple weapon?')
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
		proficiences+=[str(query('Choose a musical instrument to become proficient in:'))]
		proficiences+=[str(query('Choose another musical instrument to become proficient in:'))]
		proficiences+=[str(query('Choose a third musical instrument to become proficient in:'))]
		skillOne=str(query('Choose a skill you\'re not already proficient in: '))
		skillTwo=str(query('Choose a different skill you\'re not already proficient in: '))
		skillThree=str(query('Choose a third skill you\'re not already proficient in '))
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 to choose the third if there is one.')
		equipmentChoice=query('Would you like a rapier, a longsword, or any simple weapon?')
		if equipmentChoice==1:
			equipment+=['rapier']
		elif equipmentChoice==2:
			equipment+=['longsword']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=query('Would you like a diplomat\'s pack or and entertainer\'s pack?')
		if equipmentChoice==1:
			equipment+=['diplomat\'s pack']
		else:
			equipment+=['entertainer\'s pack']
		equipmentChoice=query('Would you like a lute or another musical instrument?')
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
		skillOne=str(query('Choose a skill: History, Insight, Medicine, Persuasion, or Religion '))
		skillTwo=str(query('Choose another skill from above:'))
		while skillTwo.lower()==skillOne.lower():
			skillTwo=str(query('Choose another skill from above:'))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=query('Would you like a Mace or a Warhammer (choose warhammer only if you\'re a Dwarf) ')
		if equipmentChoice==1:
			equipment+=['mace']
		else:
			equipment+=['warhammer']
		equipmentChoice=query('Would you like scale mail or leather armor?')
		if equipmentChoice==1:
			equipment+=['scale mail']
		else:
			equipment+=['leather armor']
		equipmentChoice=query('Would you like a light crossbow and 20 bolts or any simple weapon? ')
		if equipmentChoice==1:
			equipment+=['light crossbow and 20 bolts']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=query('Would you like a priest\'s pack or an explorer\'s pack? ')
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
		skillOne=str(query('Choose a skill from the following: Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival'))
		skillTwo=str(query('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=query('Would you like a wooden shield or any simple weapon? ')
		if equipmentChoice==1:
			equipment+=['wooden shield']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=query('Would you like a scimitar or any simple melee weapon?')
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
		skillOne=str(query('Choose a skill from the following: Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, or Survival'))
		skillTwo=str(query('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=query('Would you like chain mail or leather armor, a longbow, and 20 arrows? ')
		if equipmentChoice==1:
			equipment+=['chain mail']
		else:
			equipment+=['leather armor','longbow','twenty arrows']
		equipmentChoice=query('Would you like a martial weapon and a shield or 2 martial weapons?')
		if equipmentChoice==1:
			equipment+=['martial weapons','shield']
		else:
			equipment+=['two martial weapons']
		equipmentChoice=query('Would you like a light crossbow and 20 bolts or two handaxes? ')
		if equipmentChoice==1:
			equipment+=['light crossbow', '20 bolts']
		else:
			equipment+=['two handaxes']
		equipmentChoice=query('Would you like a dungeoneer\'s pack or an explorer\'s pack? ')
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
		proficiences+=[str(query('Choose a type of artisan\'s tools or a musical instrument to be proficient with: '))]
		savingThrows=[0,1]
		skillOne=str(query('Choose a skill from the following: Acrobatics, Athletics, History, Insight, Religion, or Stealth'))
		skillTwo=str(query('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=query('Would you like a shortsword or any simple weapon? ')
		if equipmentChoice==1:
			equipment+=['shortsword']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=query('Would you like a dungeoneer\'s pack or an explorer\'s pack? ')
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
		skillOne=str(query('Choose a skill from the following: Atheltics, Insight, Intimidation, Medicine, Persuasion, or Religion'))
		skillTwo=str(query('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=query('Would you like a martial weapon and a shield or 2 martial weapons?')
		if equipmentChoice==1:
			equipment+=['martial weapons','shield']
		else:
			equipment+=['two martial weapons']
		equipmentChoice=query('Would you like five javelins or any simple melee weapon? ')
		if equipmentChoice==1:
			equipment+=['light crossbow', '20 bolts']
		else:
			equipment+=['two handaxes']
		equipmentChoice=query('Would you like a priest\'s pack or an explorer\'s pack? ')
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
		skillOne=str(query('Choose a skill from the following: Animal Handling, Atheltics, Insight, Investigation, Nature, Perception, Stealth, or Survival'))
		skillTwo=str(query('Choose a different skill from the above: '))
		skillThree=str(query('Choose a third skill from the above: '))
		proficiences+=[skillOne,skillTwo,skillThree]
		print('For the next few options, enter 1 to choose the first option, and 2 to choose the second.')
		equipmentChoice=query('Would you like scale mail or leather armor?')
		if equipmentChoice==1:
			equipment+=['scale mail']
		else:
			equipment+=['leather armor']
		equipmentChoice=query('Would you like two shortswords or two simple melee weapons? ')
		if equipmentChoice==1:
			equipment+=['two shortswords']
		else:
			equipment+=['two simple melee weapons']
		equipmentChoice=query('Would you like a dungeoneer\'s pack or an explorer\'s pack? ')
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
		skillOne=str(query('Choose a skill from the following: Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, or Stealth'))
		skillTwo=str(query('Choose a different skill from the above: '))
		skillThree=str(query('Choose a third skill from the above: '))
		skillFour=str(query('Choose a fourth skill from the above: '))
		proficiences+=[skillOne,skillTwo,skillThree,skillFour]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=query('Would you like a rapier or a shortsword?')
		if equipmentChoice==1:
			equipment+=['rapier']
		else:
			equipment+=['shortsword']
		equipmentChoice=query('Would you like a shortbow and 20 arrows or a shortsword? ')
		if equipmentChoice==1:
			equipment+=['shortbow', '20 arrows']
		else:
			equipment+=['shortsword']
		equipmentChoice=query('Would you like a burglar\'s pack, a dungeoneer\'s pack, or an explorer\'s pack? ')
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
		skillOne=str(query('Choose a skill from the following: Arcana, Deception, Insight, Intimidation, Persuasion, or Religion'))
		skillTwo=str(query('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=query('Would you like a light crossbow and 20 bolts or any simple weapon')
		if equipmentChoice==1:
			equipment+=['light crossbow','20 bolts']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=query('Would you like a component pouch or an arcane focus? ')
		if equipmentChoice==1:
			equipment+=['component pouch']
		else:
			equipment+=['arcane focus']
		equipmentChoice=query('Would you like a dungeoneer\'s pack, or an explorer\'s pack? ')
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
		skillOne=str(query('Choose a skill from the following: Arcana, Deception, History, Intimidation, Investigation, History, or Religion'))
		skillTwo=str(query('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=query('Would you like a light crossbow and 20 bolts or any simple weapon')
		if equipmentChoice==1:
			equipment+=['light crossbow','20 bolts']
		else:
			equipment+=['any simple weapon']
		equipmentChoice=query('Would you like a component pouch or an arcane focus? ')
		if equipmentChoice==1:
			equipment+=['component pouch']
		else:
			equipment+=['arcane focus']
		equipmentChoice=query('Would you like a dungeoneer\'s pack, or a scholar\'s pack? ')
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
		skillOne=str(query('Choose a skill from the following: Arcana, History, Insight, Investigation, Medicine, or Religion'))
		skillTwo=str(query('Choose a different skill from the above: '))
		proficiences+=[skillOne,skillTwo]
		print('For the next few options, enter 1 to choose the first option, 2 to choose the second, and 3 if you want the third')
		equipmentChoice=query('Would you like a quarterstaff or a dagger')
		if equipmentChoice==1:
			equipment+=['quarterstaff']
		else:
			equipment+=['dagger']
		equipmentChoice=query('Would you like a component pouch or an arcane focus? ')
		if equipmentChoice==1:
			equipment+=['component pouch']
		else:
			equipment+=['arcane focus']
		equipmentChoice=query('Would you like a explorer\'s pack, or a scholar\'s pack? ')
		if equipmentChoice==1:
			equipment+=['explorer\'s pack']
		else:
			equipment+=['scholar\'s pack']
		equipment+=['a spellbook']

	scores=[]
	for i in range(6):
		nums=[]
		for i in range(4):
			nums.append(randint(1,6))
		nums[nums.index(min(nums))]=0
		scores.append(sum(nums))

	print('Your scores are',str(scores[0])+',',str(scores[1])+',',str(scores[2])+',',str(scores[3])+',',str(scores[4])+',',str(scores[5]))
	print('Your race buffs are +'+str(asi[0])+' to Strength, +'+str(asi[1])+' to Dexterity, +'+str(asi[2])+' to Constitution, +'+str(asi[3])+' to Wisdom, +'+str(asi[4])+' to Intelligence, and +'+str(asi[5])+' to Charisma')
	strength=query('Which score would you like to use for strength? ')
	while strength not in scores:
		strength=query('That\'s not an available score. Which score would you like to use for strength? ')
	scores.remove(strength)
	dexterity=query('Which score would you like to use for dexterity? ')
	while dexterity not in scores:
		dexterity=query('That\'s not an available score. Which score would you like to use for dexterity? ')
	scores.remove(dexterity)
	constitution=query('Which score would you like to use for constitution? ')
	while constitution not in scores:
		constitution=query('That\'s not an available score. Which score would you like to use for constitution? ')
	scores.remove(constitution)
	wisdom=query('Which score would you like to use for wisdom? ')
	while wisdom not in scores:
		wisdom=query('That\'s not an available score. Which score would you like to use for wisdom? ')
	scores.remove(wisdom)
	intelligence=query('Which score would you like to use for intelligence? ')
	while intelligence not in scores:
		intelligence=query('That\'s not an available score. Which score would you like to use for intelligence? ')
	scores.remove(intelligence)
	charisma=scores[0]+asi[5]
	strength+=asi[0]
	dexterity+=asi[1]
	constitution+=asi[2]
	wisdom+=asi[3]
	intelligence+=asi[4]
	print('Your scores are: ')
	print('Strength:',strength)
	print('Dexterity:',dexterity)
	print('Constitution:',constitution)
	print('Wisdom:',wisdom)
	print('Intelligence:',intelligence)
	print('Charisma:',charisma)
	playerName=query('What is your name? ')
	characterName=query('What would you like to name your character?')

	strMod = int(floor((strength - 10)/2))
	dexMod = int(floor((dexterity - 10)/2))
	conMod = int(floor((constitution - 10)/2))
	intMod = int(floor((intelligence - 10)/2))
	wisMod = int(floor((wisdom - 10)/2))
	chaMod = int(floor((charisma - 10)/2))

	AC=10+dexMod
	if userClass=='monk':
		AC=10+dexMod+wisMod
	elif userClass=='barbarian':
		AC=10+dexMod+conMod
	if 'leather armor' in equipment:
		AC=11+dexMod
	elif 'scale mail' in equipment:
		if dexMod>=2:
			AC=16
		else:
			AC=14+dexMod
	elif 'chain mail' in equipment:
		AC=16
	if 'shield' in equipment:
		AC+=2
	elif 'wooden shield' in equipment:
		AC+=2

	fields = [('ClassLevel', userClass + " 1"),
		  ('PlayerName',playerName),
		  ('CharacterName',characterName),
		  ('Race ',userRace + ' (' + subType + ')'),
		  ('XP','0'),
		  ('STR',str(strength)),
		  ('ProfBonus','+2'),
		  ('AC',str(AC)),
		  ('Initiative',str(dexMod)),
		  ('Speed',str(walkingSpeed)),
		  ('STRmod',str(strMod)),
		  ('HPMax',str(hpMax + conMod)),
		  ('ST Strength',str(strMod + (2 if (0 in savingThrows) else 0))),
		  ('DEX',str(dexterity)),
		  ('DEXmod ',str(dexMod)),
		  ('CON',str(constitution)),
		  ('HDTotal','1d' + str(hitDice)),
		  ('CONmod',str(conMod)),
		  ('INT',str(intelligence)),
		  ('ST Dexterity',str(dexMod + (2 if (1 in savingThrows) else 0))),
		  ('ST Constitution',str(conMod + (2 if (2 in savingThrows) else 0))),
		  ('ST Intelligence',str(intMod + (2 if (3 in savingThrows) else 0))),
		  ('ST Wisdom',str(wisMod + (2 if (4 in savingThrows) else 0))),
		  ('ST Charisma',str(chaMod + (2 if (5 in savingThrows) else 0))),
		  ('Acrobatics',str(dexMod + (2 if 'Acrobatics' in proficiencies else 0))),
		  ('Animal',str(wisMod + (2 if 'Animal Handling' in proficiencies else 0))),
		  ('Athletics',str(strMod + (2 if 'Athletics' in proficiencies else 0))),
		  ('Deception ',str(chaMod + (2 if 'Deception' in proficiencies else 0))),
		  ('History ',str(intMod + (2 if 'History' in proficiencies else 0))),
		  ('Insight',str(wisMod + (2 if 'Insight' in proficiencies else 0))),
		  ('Intimidation',str(chaMod + (2 if 'Intimidation' in proficiencies else 0))),
		  ('INTmod',str(intMod)),
		  ('Investigation ',str(intMod + (2 if 'Investigation' in proficiencies else 0))),
		  ('WIS',str(wisdom)),
		  ('Arcana',str(intMod + (2 if 'Arcana' in proficiencies else 0))),
		  ('Perception ',str(wisMod + (2 if 'Perception' in proficiencies else 0))),
		  ('WISmod',str(wisMod)),
		  ('CHA',str(charisma)),
		  ('Nature',str(intMod + (2 if 'Nature' in proficiencies else 0))),
		  ('Performance',str(chaMod + (2 if 'Performance' in proficiencies else 0))),
		  ('Medicine',str(wisMod + (2 if 'Medicine' in proficiencies else 0))),
		  ('Religion',str(intMod + (2 if 'Religion' in proficiencies else 0))),
		  ('Stealth ',str(dexMod + (2 if 'Stealth' in proficiencies else 0))),
		  ('Persuasion',str(chaMod + (2 if 'Persuasion' in proficiencies else 0))),
		  ('SleightofHand',str(dexMod + (2 if 'Sleight of Hand' in proficiencies else 0))),
		  ('CHamod',str(chaMod)),
		  ('Survival',str(wisMod + (2 if 'Survival' in proficiencies else 0))),
		  ('Passive',str(10 + wisMod + (2 if 'Perception' in proficiencies else 0))),
		  ('ProficienciesLang',', '.join(proficiencies + languages),
		  ('Equipment',', '.join(equipment)),
		  ('Features and Traits',', '.join(attributes)),
		  ('CharacterName 2',characterName),
		  ('Backstory',backstory),
		  ('Check Box 11','Yes' if 0 in savingThrows else 'No'), # Strength ST Prof
		  ('Check Box 18','Yes' if 1 in savingThrows else 'No'), # Dexterity ST Prof
		  ('Check Box 19','Yes' if 2 in savingThrows else 'No'), # Constitution ST Prof
		  ('Check Box 20','Yes' if 3 in savingThrows else 'No'), # Intelligence ST Prof
		  ('Check Box 21','Yes' if 4 in savingThrows else 'No'), # Wisdom ST Prof
		  ('Check Box 22','Yes' if 5 in savingThrows else 'No'), # Charisma ST Prof
		  ('Check Box 23','Yes' if 'Acrobatics' in proficiencies else 'No'), # Acrobatics Prof
		  ('Check Box 24','Yes' if 'Animal Handling' in proficiencies else 'No'), # Animal Handling Prof
		  ('Check Box 25','Yes' if 'Arcana' in proficiencies else 'No'), # Arcana Prof
		  ('Check Box 26','Yes' if 'Athletics' in proficiencies else 'No'), # Athletics Prof
		  ('Check Box 27','Yes' if 'Deception' in proficiencies else 'No'), # Deception Prof
		  ('Check Box 28','Yes' if 'History' in proficiencies else 'No'), # History Prof
		  ('Check Box 29','Yes' if 'Insight' in proficiencies else 'No'), # Insight Prof
		  ('Check Box 30','Yes' if 'Intimidation' in proficiencies else 'No'), # Intimidation Prof
		  ('Check Box 31','Yes' if 'Investigation' in proficiencies else 'No'), # Investigation Prof
		  ('Check Box 32','Yes' if 'Medicine' in proficiencies else 'No'), # Medicine Prof
		  ('Check Box 33','Yes' if 'Nature' in proficiencies else 'No'), # Nature Prof
		  ('Check Box 34','Yes' if 'Perception' in proficiencies else 'No'), # Perception Prof
		  ('Check Box 35','Yes' if 'Performance' in proficiencies else 'No'), # Performance Prof
		  ('Check Box 36','Yes' if 'Persuasion' in proficiencies else 'No'), # Persuasion Prof
		  ('Check Box 37','Yes' if 'Religion' in proficiencies else 'No'), # Religion Prof
		  ('Check Box 38','Yes' if 'Sleight of Hand' in proficiencies else 'No'), # Sleight of Hand Prof
		  ('Check Box 39','Yes' if 'Stealth' in proficiencies else 'No'), # Stealth Prof
		  ('Check Box 40','Yes' if 'Survival' in proficiencies else 'No')] # Survival Prof
	fdf = forge_fdf("", fields, [], [], [])
	fdf_file = open("char_sheet.fdf", "wb")
	fdf_file.write(fdf)
	fdf_file.close()
	os.system("pdftk EmptyCharacterSheet.pdf fill_form char_sheet.fdf output char_sheet.pdf")


