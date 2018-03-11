import pickle

from sklearn.pipeline import Pipeline

import prettyprinters as pp
# import characterCreation as cc

balanced=False
race_lut = ['dwarf', 'elf', 'halfling', 'human', 'dragonborn', 'gnome', 'half-elf', 'half-orc', 'tiefling']
class_lut = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']


def main():
	if balanced:
		f = open('ml-magic/class_balanced_pipeline', 'rb')
		class_pipeline = pickle.load(f)
		f.close()
		f = open('ml-magic/race_balanced_pipeline', 'rb')
		race_pipeline = pickle.load(f)
		f.close()
	else:
		f = open('ml-magic/class_unbalanced_pipeline', 'rb')
		class_pipeline = pickle.load(f)
		f.close()
		f = open('ml-magic/race_unbalanced_pipeline', 'rb')
		race_pipeline = pickle.load(f)
		f.close()
		
	pp.head('Welcome to the D&D Character Setup Helper!')

	pp.description(
"""This tool will walk you through the process of creating their first
Dungeons and Dragons character sheet. The first stepis to think of a
backstory for your character. Your backstory should describe where your
character came from, what motivates them, and what their goals and
deals are. We'll try to use your backstory to make some suggestions for
how to design your character.""")

	backstory = pp.query('Type in your backstory:')

	suggested_race = race_lut[race_pipeline.predict([backstory])[0]]
	suggested_class = class_lut[class_pipeline.predict([backstory])[0]]

	pp.description("""
From your backstory, it looks like you'd make a great {} {}.""".format(suggested_race,suggested_class))

	cc.characterCreation(suggested_race, suggested_class, backstory)

	# pp.description(suggested_class)
	# pp.description(suggested_race)


if __name__ == '__main__':
	main()