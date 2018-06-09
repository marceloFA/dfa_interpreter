#Módulo de expressões regulares
import re
#Faz prints coloridos
from termcolor import colored # pip install termcolor
#expresões regulares que leem a definição e as transições de um autômato: 
automata_regex = re.compile(r'\(\{([a-z],?\s?)+\},\s\{\s?((q([0-9]|f)),?\s?)+\},\s[A-Z],\s(q[0-9]){1},\s\{\s?((q([0-9]|f)),?\s?)+\}\)')
trasitions_regex = re.compile(r'(q([0-9]|f)),\s([a-z]),\s(q([0-9]|f))\n?')

#Lê o conteúdo de um arquivo:
def read_content(file_name):
    with open(file_name,'r') as f:
        content = f.read()
        return content

def validate_to_str(regex,content):
    matches = re.finditer(regex,content)
    results = [match.group(0) for match in matches]
    
    #for x in results:
        #print(x)
    return results

# Define o estado inicial:
def parse_inicial_state(definition):
    regex = re.compile(r'(q[0-9]){1},\s')
    temp = definition.split('},')[2]
    return validate_to_str(regex,temp)[0][1:2]

#Define o conjuntod eestados finais:
def parse_final_states(definition):
    #get only final states:
    regex = re.compile(r'\{\s?((q([0-9]|f)),?\s?)+\}\)')
    temp = validate_to_str(regex,definition)[0]
    #parse only numbers to set:
    regex = re.compile(r'(f|[0-9])+')
    temp = validate_to_str(regex,temp)
    finals = set(temp)
    return finals

#transoforma um estado  chamado 'f' para um estado chamado 'n+1'
#onde n é o número mais alto associado a um estado


def parse_transitions(transitions):
    #Encontre somente os estados únicos:
    unique_states = []
    for transition in transitions:
        unique_states.append(transition[1])
    unique_states = list(set(unique_states))
    #Adicione estes estados como chaves de um dicionário:
    temp = {}
    for state in unique_states:
        temp[state] = {}
        for transition in transitions:
            if transition[1] == state:
                word = transition[4]
                temp[state][word] = transition[8]
    return temp

#A função que processa o autômato:
def process(transitions,initial,finals,word):
    state = initial
    #Para cada símbolo na palavra:
    for s in word:
        #Se o estado possui transições:
        if state in list(transitions.keys()):
            #Se houver uma transição que processa o símbolo atual:
            if s in list(transitions[state].keys()):
                state = transitions[state][s]
            else:
                return False
        else:
            return False
    return state in finals




# A função principal:
def main(file_name,word):
    #Lê o conteúdo
    content = read_content(file_name)
    print("O conteudo do arquivo lido é:\n")
    print(content+'\nSe sua definição estiver nos conformes, a palavra será processada com sucesso\n\n')
    #Procura pela definição:
    definition = validate_to_str(automata_regex,content)[0]
    #procura pelas transições:
    transitions = validate_to_str(trasitions_regex,content)
    #Define o estado inicial:
    initial = parse_inicial_state(definition)
    #Define o conjunto de estados finais:
    finals = parse_final_states(definition)
    #Tranições para dicionário:
    transitions = parse_transitions(transitions)

    if process(transitions,initial,finals,word):
        print("A palavra foi "+ colored('aceita', 'green')+ " ao final do processamento!")
    else:
        print("A palavra foi "+ colored('rejeitada', 'red')+" ao final do processamento!")

    return


#O script final:
print("Insira o nome do arquivo a ser processado, incluindo extensão:")
file_name = input("(use como exemplo de testes AFD.txt)\n")
word = input("Insira a palavra a ser processada:")
main(file_name,word)
