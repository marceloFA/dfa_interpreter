# Exemplo descaradamente copiado da pagina do projeto e adaptado pelo autor
'''
algumas coisas pra fazer antes de isso rodar:
pip3 install easygui
sudo apt-get install python3-tk
'''

'''
Para travbalhar depois:
http://easygui.readthedocs.io/en/latest/_modules/easygui/boxes/fileopen_box.html
'''

import easygui, sys

easygui.msgbox("Hello, world!")

while 1:

  msg ="Qual o seu sabor favorito?"
  title = "Uma pesquisa sobre sorvetes"
  choices = ["Baunilha", "Chocolate", "Morango", "Flocos"]
  choice = easygui.choicebox(msg, title, choices)

  # note a conversao para string de choice abaixo, 
  # porque o usuario pode ter cancelado a escolha,
  # dessa forma o resultado seria None
  easygui.msgbox("Voce escolheu: " + str(choice), " como resultado da pesquisa.")

        

  msg = "Voce gostaria de continuar?"
  title = "Confirmacao"
  if easygui.ccbox(msg, title):     # Um dialogo "Continue/Cancel"
    pass  # Se o luser escolher continue, o dialogo retorna "true"
  else:
    sys.exit(0)           # do contrario...