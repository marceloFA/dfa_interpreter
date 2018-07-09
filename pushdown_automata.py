import json
import re
from termcolor import colored # pip install termcolor

#expresões regulares que leem a definição e as transições de um autômato com pilha: 
pushdown_automata_regex = re.compile(r'\(\{([a-z],?\s?)+\},\s\{\s?((q([0-9]{1,2}|f)),?\s?)+\},\s[A-Z],\s(q[0-9]{1,2}){1},\s\{\s?((q([0-9]{1,2}|f)),?\s?)+\},\s\{([A-Z],?\s?)+\}\)')
trasitions_regex = re.compile(r'(q([0-9]|f)),\s(([a-z])|\?),\s(([A-Z])|\?),\s(q([0-9]|f))\n?,\s(([A-Z])|\_)')

#Lê o conteúdo de um arquivo:
def read_content(file_name):
    with open(file_name,'r') as f:
        content = f.read()
        return content

#valida um conteúdo, baseado em uma regex:
def validate_to_str(regex,content):
    matches = re.finditer(regex,content)
    results = [match.group(0) for match in matches]
    #for x in results: #caso queira ver os resultados
        #print(x)
    return results

# Define o estado inicial:
def parse_inicial_state(definition):
    #Acha a definição do estado inicial:
    regex = re.compile(r'D,\s(q[0-9]{1,2}){1}')
    temp = validate_to_str(regex,definition)[0]
    #Agora tira só o numerozin:
    regex = re.compile(r'([0-9]{1,2})')
    return validate_to_str(regex,temp)[0]

#Define os estados finais:    
def parse_final_states(definition):
    #REGEX pra achar os estados finais (ou iniciais):
    regex = re.compile(r'\{\s?((q([0-9]{1,2}|f)),?\s?)+\}')
    #como essa regex acha os iniciais tbm, os finais são o segundo match, index 1
    temp = validate_to_str(regex,definition)[1]
    #parse only numbers to set:
    regex = re.compile(r'(f|[0-9]{1,2})+')
    temp = validate_to_str(regex,temp)
    finals = set(temp)
    return finals

def parse_transitions(transitions)
	#teste a REGEX das transições:;
	#ache um jeito de salvar as transições em um dictionary;
	return transitions

##ESTADO ATUAL: TRABALHANDO NA FUNÇÃO Q FAZ O PARSING DAS TRANSIÇÕES:
def main(file_name):
    #Lê o conteúdo:
    content = read_content(file_name)
    definition = validate_to_str(pushdown_automata_regex,content)[0]
    initial = parse_inicial_state(definition)
    finals = parse_final_states(definition)
    transitions = validate_to_str(trasitions_regex,content)

    print("O conteudo do arquivo lido é:\n")
    print(content) 
    print("A definição é:\n")
    print(definition)
    print('\n\nO estado incial é: q'+initial+'\n')
    print("Os estados finais são:")
    print(finals)
    print("As transições são:")
    return



#O script principal:
print("Insira o nome do arquivo a ser processado, incluindo extensão:")
file_name = input("(use como exemplo de testes AFD.txt)\n")
main(file_name)
