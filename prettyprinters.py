
from clint.textui import puts, indent, colored, prompt

class bcolors:
	QUERY = '\033[36m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	ENDBOLD = '\033[22m'

def query(text):
	res = prompt.query(bcolors.QUERY+text+bcolors.ENDC)
	return res

def description(text):
	# puts('')
	with indent(4):
		puts(colored.green(text))
	puts('')

def head(text):
	puts('')
	with indent(8):
		puts(colored.blue(bcolors.BOLD+text+bcolors.ENDBOLD))
	puts('')


