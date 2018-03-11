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