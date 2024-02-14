# Capítulo 8 
# Questões 8.15 e 8.16

# Possibilitando o import de outras pastas
import sys
sys.path.append('../Capitulo_2_8')

import atividades as atv

# Outras possibilidades de import
# import atividades
# from atividades import imprime_mensagem_simples_21
# from atividades import imprime_mensagem_simples_21 as print_message
# from atividades import *

# Chamando a primeira função criada no arquivo de atividades
atv.imprime_mensagem_simples_21()