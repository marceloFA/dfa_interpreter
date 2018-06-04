import re
automata_regex = re.compile(r'\(\{([a-z],?\s?)+\},\s\{\s?((q([0-9]|f)),?\s?)+\},\s[A-Z],\s(q[0-9]){1},\s\{\s?((q([0-9]|f)),?\s?)+\}\)')
trasitions_regex = re.compile(r'(q([0-9]|f)),\s([a-z]),\s(q([0-9]|f))\n?')

def read_content():
	with open('AFD.txt','r') as f:
		content = f.read()
		return content

def validate_to_str(regex,content):
	matches = re.finditer(regex,content)
	results = [match.group(0) for match in matches]
	
	for x in results:
		print(x)
	return results

def parse_inicial_state(definition):
	regex = re.compile(r'(q[0-9]){1},\s')
	temp = definition.split('},')[2]
	return int(validate_to_str(regex,temp)[0][1:2])


def parse_final_states(definition):
	finals = {}
	#get only final states:
	regex = re.compile(r'\{\s?((q([0-9]|f)),?\s?)+\}\)')
	temp = validate_to_str(regex,definition)[0]
	#parse only numbers to set:
	regex = re.compile(r'(f|[0-9])+')
	temp = '{qf, q1, q2, q3})'
	temp = validate_to_str(regex,temp)
	print(temp)
	finals = set(temp)
	return finals

def parse_transitions():
	#essa vai ser foda de escrever
	return



content = read_content()
definition = validate_to_str(automata_regex,content)[0] #fix this later
transitions = validate_to_str(trasitions_regex,content)
initial_state = parse_inicial_state(definition)
final_states = parse_final_states(definition)