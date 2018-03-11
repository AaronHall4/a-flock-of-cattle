from fdfgen import forge_fdf
import os
from math import floor

# TODO: Include weapon stuff

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

fields = [
          ('ClassLevel', userClass + " 1"),
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
          ('Check Box 40','Yes' if 'Survival' in proficiencies else 'No'), # Survival Prof
          ]
fdf = forge_fdf("", fields, [], [], [])
fdf_file = open("char_sheet.fdf", "wb")
fdf_file.write(fdf)
fdf_file.close()
os.system("pdftk EmptyCharacterSheet.pdf fill_form char_sheet.fdf output char_sheet.pdf")
