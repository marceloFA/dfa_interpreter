'''
Links úteis:
Como usar expresões regulares:
https://www.regular-expressions.info/quickstart.html
https://www.youtube.com/watch?v=sa-TUpSx1JA #Assista esse primeiro!!

Como usar expresões regulares com Python:
https://www.youtube.com/watch?v=K8L6KVGG-7o


Tópico no StackOverflow sobre processamento de autômatos com python:
https://stackoverflow.com/questions/35272592/how-are-finite-automata-implemented-in-code
'''

import re # lida com expressões regulares

#Exemplo de expressões regulares usadas para ler um automato:
automata = '({a, b}, {q0, q1, q2, qf}, D, q0, {qf})'
#trasições:
D = '''
	q0, a, q1
	q1, a, qf
	q0, b, q2
	q1, b, q2
	''' 
# (q([0-9]|f)),\s([a-z]),\s(q([0-9]|f))\n?

symbols = '({a,b}, ' # \(\{([a-z],?\s?)+\},\s
states = '{q0, q1, q2, qf}, ' # \{\s?((q([0-9]|f)),?\s?)+\},\s
transitions = 'D, ' # D,\s
inicial_state = 'q0, ' #(q[0-9]){1},\s
final_states = '{qf, q1, q2, q3})' # \{\s?((q([0-9]|f)),?\s?)+\}\) #adicione um \n no final disso depois


'''
Uma expressão regular completa para ler a definição do automato:
\(\{([a-z],?\s?)+\},\s\{\s?((q([0-9]|f)),?\s?)+\},\s[A-Z],\s(q[0-9]){1},\s\{\s?((q([0-9]|f)),?\s?)+\}\)

OBS: essa expressão precisa passar por testes!
final_states must be a set
'''





#funções auxiliares do parser que virá a seguir:
def to_dictionary(inn):
	return


automata_regex = re.compile(r'\(\{([a-z],?\s?)+\},\s\{\s?((q([0-9]|f)),?\s?)+\},\s[A-Z],\s(q[0-9]){1},\s\{\s?((q([0-9]|f)),?\s?)+\}\)')

#Uma função que lê um AFD de um arquivo e salva em uma variável:
def read_content():
	with open('AFD.txt','r') as f:
		content = f.read()
		return content


#a função que transforma texto em um automato:
def parse_to_automata():
	automata_def = []
	content = read_content()
	#print(content) 
	matches = automata_regex.finditer(content)
	for match in matches:
		automata_def.append(match)
	print(automata_def)
	return


#Exemplo de como o autômato deve ficar após passar pelo parser:
dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}


#A função que processa o autômato:
def processa(transicoes,inicial,aceitos,s):
    estado = inicial
    for c in s:
        estado = transicoes[estado][c]
    return estado in aceitos


#Exemplo de uso:
if processa(dfa,0,{0},'1011101'):
	print("Aceito!\n")
else:
	print("Não Aceito!\n")

#Exemplo de uso 2:
if processa(dfa,0,{0},'10111011'):
	print("Aceito!\n")
else:
	print("Não Aceito!\n")

