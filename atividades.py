# Capítulo 2

# Imprime uma mensagem simples através de uma variável e a função print
def imprime_mensagem_simples_21():
    mensagem = 'Hello World!'
    print(mensagem)

# Dá um valor a uma variável e a imprime, depois troca o valor desta e a imprime novamente
def imprime_duas_mensagens_22():
    mensagem = 'Primeira mensagem.'
    print(mensagem)
    mensagem = 'Segunda mensagem.'
    print(mensagem)

def mensagem_pessoal_23():
    pessoa = 'Ana'
    print(f'Te amo, {pessoa}')

def maiuscula_minuscula_24():
    pessoa = 'Rafael'
    print(pessoa.lower())
    print(pessoa.upper())
    print(pessoa.title())

def citacao_famosa_25():
    mensagem = 'Albert Einstein disse uma vez: "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo".'
    print(mensagem)

def citacao_famosa_2_26():
    famous_person = 'Albert Einstein'
    mensagem = f'{famous_person} disse uma vez: "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo".'
    print(mensagem)

def removendo_nomes_27():
    nome_pessoa = ' \r\tBreno\n '
    print(nome_pessoa)
    print(nome_pessoa.strip())
    print(nome_pessoa.rstrip())
    print(nome_pessoa.lstrip())

def extensoes_arquivos_28():
    filename = 'python_notes.txt'
    print(filename.removesuffix('.txt'))

def numero_oito_29():
    print(4+4)
    print(10-2)
    print(2*4)
    print(16*0.5)
    
def numero_favorito_210():
    numero_favorito = 27
    print(f'Meu número favorito é {numero_favorito}')

def adicionando_comentarios_211():
    # Comentários foram adicionados a duas das funções deste programa
    pass

# Capítulo 3

def nomes_31():
    nomes = ['ed', 'thigas', 'yago', 'cup']
    print('\n'.join(nomes).title())

def cumprimentos_32():
    nomes = ['ed', 'thigas', 'yago', 'cup']
    mensagem = '{} é um camarada.'
    for nome in nomes:
        print(mensagem.format(nome.title()))

def propria_lista_33():
    carros = ['Koenigsegg Agera RS', 'Lamborghini Gallardo', 'Aston Martin Valkyrie']
    mensagem = 'Eu adoraria ter um {}.'
    for carro in carros:
        print(mensagem.format(carro))

def lista_convidados_34():
    convidados = [
        'albert einstein',
        'stephen hawking',
        'eduardo saverin',
        'jeff bezos'
    ]
    mensagem = 'Adoraria que comparecesse em meu jantar, {}.'

    for convidado in convidados:
        print(mensagem.format(convidado))
    
    return convidados, mensagem

import random
def mudando_lista_convidados_35():
    convidados, mensagem = lista_convidados_34()
    indice_faltante = (random.randint(0, len(convidados) - 1))
    print(f'{convidados[indice_faltante].title()} não comparecerá ao jantar.')
    convidados[indice_faltante] = 'mark zuckerberg'
    print(mensagem.format(convidados[indice_faltante].title()))

def mais_convidados_36():
    convidados, mensagem = lista_convidados_34()
    print('Foi encontrada uma mesa maior.')
    convidados.insert(0, 'mark zuckerberg')
    convidados.insert(len(convidados) // 2, 'elon musk')
    convidados.append('kunimitsu takahashi')
    for convidado in convidados:
        print(mensagem.format(convidado.title()))
    
    return convidados, mensagem

def reduzindo_lista_convidados_37():
    convidados, mensagem = mais_convidados_36()
    print('Apenas duas pessoas poderão ser convidadas para o jantar. :(')

    while len(convidados) > 2:
        print(f'Desculpe, {convidados.pop().title()}, mas o jantar foi cancelado. :(')

    for convidado in convidados:
        print(f'A festa continua. Espero sua presença, {convidado.title()}.')

def conhecendo_mundo_38():
    lugares = ['monte everest', 'andes', 'caribe', 'cancun', 'fernando de noronha']
    print(' - '.join(x.title() for x in lugares))
    print(' - '.join(sorted(x.title() for x in lugares)))
    lugares.reverse()
    print(' - '.join(x.title() for x in lugares))
    lugares.reverse()
    print(' - '.join(x.title() for x in lugares))
    lugares.sort()
    print(' - '.join(x.title() for x in lugares))
    lugares.sort(reverse=True)
    print(' - '.join(x.title() for x in lugares))   

def convidados_jantar_39():
    convidados, mensagem  = lista_convidados_34()
    print(f'{len(convidados)} pessoas estão sendo convidados para o jantar.')

def funcoes_310():
    armas = [
        'Accuracy International AS50',
        'Ag m/42',
        'AGM-1 Carbine',
        'AK-74',
        'AK74U',
        'Benelli Argo EL',
        'Benelli MR1',
        'Beretta BM59',
        'Beretta Cx4 Storm',
        'Bushmaster M4 Type Carbine',
        'Carbon 15',
        'Charlton Automatic Rifle',
        'FN Scar-H SV',
        'FN Model 1949',
        'Fusil Automatique Modèle 1917',
        'General Liu rifle',
        'German Sport Guns GSG-5',
        'Gewehr 41',
        'Heckler & Koch HK41',
        'Heckler & Koch HK43',
        'Heckler & Koch PSG1',
        'Heckler & Koch SL7',
        'Hi-Point Carbine',
        'Howa Type 64',
        'Howard Francis machine carbine',
        'Howell Automatic Rifle',
        'Kbsp wz. 1938M',
        'Kintrek KBP-1',
        'L1A1 Self-Loading Rifle',
        'M110 Semi-Automatic Sniper System',
        'M4A1',
        'M4A4',
        'M89SR sniper rifle',
        'Norinco JW-20',
        'MG 42',
        'MP 40',
        'Norinco NHM 91',
        'Olin/Winchester Salvo Rifle',
        'P90',
        'PP2000',
        'Pauza P-50',
        'Pedersen rifle',
        'Preetz Model 65',
        'PSL (rifle)',
        'PTR 91F',
        'QBU-88',
        'Rasheed Carbine',
        'Remington Model 24',
        'Remington Model 522 Viper',
        'Remington Nylon 66',
        'Remington Semi Automatic Sniper System',
        'Rieder Automatic Rifle',
        'Ruger SR-556',
        'Smith & Wesson M&P10',
        'Smith & Wesson M&P15',
        'Smith & Wesson M&P15-22',
        'Steyr IWS 2000',
        'UMP45',
        'Volkssturmgewehr',
        'Vulcan V18',
        'Vz. 52 rifle',
        'Walther G22',
        'Walther WA 2000',
        'Winchester model 30',
        'Zastava M91',
        'Zijiang M99'
    ]

    print(f'Total de armas: {len(armas)}')
    print('  ︻┳═一 \n'.join(armas))

    for _ in range(random.randint(1, len(armas))):
        print(f'{armas.pop()} foi excluída do estoque.')

    print(f'Total de armas restantes: {len(armas)}')

    arma_a_comprar = input('Qual arma deseja comprar?')
    guns_number = armas.count(arma_a_comprar)
    if guns_number > 0:
        print(f'{arma_a_comprar} foi vendida. ︻┳═一 🛍️')
        armas.remove(arma_a_comprar)
    else:
        print(f'{arma_a_comprar} não está no estoque.')

    print('Lista de armas restantes:')
    print('  ︻┳═一 \n'.join(reversed(armas)))
    
def erro_intencional_311():
    lista = ['0']
    index = int(input('Entre com um numero maior que 0 para gerar um erro.'))
    print(lista[index])

# Capítulo 4
    
def pizzas_41():
    pizzas = ['4 queijos', 'A moda', 'Frango com Catupiry']
    for pizza in pizzas:
        print(f'Um dos sabores de pizza que gosto é {pizza.lower()}.')
    print('Eu adoro pizza.')
    return pizzas

def animais_42():
    animais = ['golfinho', 'baleia azul' ,'baleia jubarte']
    for animal in animais:
        print(f'Você sabia que {animal} não é um peixe?')
    print('Todos esses animais são mamiferos.')

def contando_ate_vinte_43():
    for i in range(1, 21):
        print(i, end='_')

def um_milhao_44():
    numeros = [(i) for i in range(1, 1_000_001)]
    for numero in numeros:
        print(numero)

def somando_um_milhao_45():
    numeros = [(i) for i in range(1, 1_000_001)]
    print(min(numeros))
    print(max(numeros))
    print(sum(numeros))

def numeros_impares_46():
    numeros_impares = [i for i in range(1, 20, 2)]
    for numero in numeros_impares:
        print(numero, end=' _ ')

def tres_47():
    multiplos_de_tres = [i for i in range(3, 30, 3)]
    for multiplo in multiplos_de_tres:
        print(multiplo, end=' _ ')

def cubos_48():
    cubos = [i**3 for i in range(1, 11)]
    for cubo in cubos:
        print(cubo, end=' _ ')

def cube_comprehension_49():
    cubos = [i**3 for i in range(1, 11)]
    for cubo in cubos:
        print(cubo, end=' _ ')

def fatias_410():
    numeros_ate_vinte = [i for i in range(1, 21)]
    comprimento = len(numeros_ate_vinte)
    primeiros_elementos = 'primeiros elementos'
    elementos_do_meio = 'elementos do meio'
    ultimos_elementos = 'ultimos elementos'
    mensagem = 'Os {} da lista são: {}'
    print(mensagem.format(primeiros_elementos, numeros_ate_vinte[0:3]))
    print(mensagem.format(elementos_do_meio, numeros_ate_vinte[(comprimento//2 - 2):(comprimento//2 + 1)]))
    print(mensagem.format(ultimos_elementos, numeros_ate_vinte[-3:]))

def minhas_pizzas_suas_pizzas_411():
    minhas_pizzas = pizzas_41()
    friends_pizzas = minhas_pizzas[:]
    minhas_pizzas.append('Pepperoni')
    friends_pizzas.append('Calabresa')
    print(f'Minhas pizzas favoritas sao: {", ".join(minhas_pizzas)}.')
    print(f'As pizzas favoritas do meu amigo sao: {", ".join(friends_pizzas)}.')   

def foods_412():
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    my_foods.append('cannoli')
    friend_foods.append('ice cream')
    print('My favorite foods are: ')
    for item in my_foods:
        print(item)
    print("\nMy friend's favorite foods are:")
    for item in friend_foods:
        print(item)

def bufet_413():
    refeicoes = ('Tropeiro', 'Miojo', 'Farofa', 'Feijoada', 'Lasanha')
    mensagem = '\nBUFFET\n'
    print(mensagem)
    for refeicao in refeicoes:
        print(refeicao)
    # refeicoes[0] = 'Alface' TypeError -> Exigido pelo exercício que o erro fosse gerado
    refeicoes_lista = list(refeicoes) 
    refeicoes_lista[random.randint(0, len(refeicoes) - 1)] = 'Peixe'
    refeicoes_lista[random.randint(0, len(refeicoes) - 1)] = 'Escondidinho'

    refeicoes = tuple(refeicoes_lista)

    print(mensagem)
    for refeicao in refeicoes:
        print(refeicao)

# Capitulo 5

def testes_condicionais_51():
    car = 'subaru'
    print('Is car == "subaru"? I predicted True.')
    print(car == 'subaru')

    print('Is car == "audi"? I predicted False.')
    print(car == 'audi')

    print('Comprimento da marca é igual a 7?')
    print(len(car) == 7)

    print('Comprimento da marca é igual a 6?')
    print(len(car) == 6)

    print(f'As primeiras 2 letras da marca são "au"?')
    print(car[0:2].lower() == 'au')

    print(f'As primeiras 2 letras da marca são "su"?')
    print(car[0:2].lower() == 'su')

def mais_testes_condicionais_52():
    print("'Matheus' != 'Rafael'?", 'Matheus' != 'Rafael')
    print("'Matheus' == 'Rafael'?", 'Matheus' == 'Rafael')
    print("'Matheus'.lower() == 'matheus'?", 'Matheus'.lower() == 'matheus')
    print('2 > 4?', 2 > 4)
    print('2 < 4?', 2 < 4)
    print('2 >= 4?', 2 >= 4)
    print('2 <= 4?', 2 <= 4)
    print('2 == 4?', 2 == 4)
    print('2 != 4?', 2 != 4)

def cores_alienigenas_53():
    alien_color = 'green'
    message = ''
    if alien_color == 'green':
        message = 'Ganhou 5 pontos.'
    print(message, end='')

def cores_alienigenas_2_54():
    alien_color = 'red'
    message = ''
    if alien_color == 'green':
        message = 'Ganhou 5 pontos.'
    else:
        message = 'Ganhou 10 pontos.'
    print(message, end='')

def cores_alienigenas_3_55():
    alien_color = 'yellow'
    message = ''

    if alien_color.lower() == 'green':
        message = 'Ganhou 5 pontos.'
    elif alien_color.lower() == 'yellow':
        message = 'Ganhou 10 pontos.'
    elif alien_color.lower() == 'red':
        message = 'Ganhou 15 pontos.'
        
    print(message, end='')

def fases_da_vida_56():
    age = int(input('Entre com sua idade: '))
    message = '';
    if age < 2:
        message = 'um neném'
    if 2 < age < 4:
        message = 'uma criança'
    if 4 < age < 13:
        message = 'um(a) garoto(a)'
    if 13 < age < 20:
        message = 'um(a) adolescente'
    if 20 < age < 65:
        message = 'um(a) adulto(a)'
    if age >= 65:
        message = 'um(a) idoso(a)'
    
    print(f'Você é {message}.')

def fruta_favorita_57():
    frutas_favoritas = [ 'carambola', 'laranja', 'mixirica']
    message = 'Você realmente gosta de {}!'

    if 'banana' in frutas_favoritas:
        print(message.format('bananas'))
    if 'mixirica' in frutas_favoritas:
        print(message.format('mixiricas'))
    if 'carambola' in frutas_favoritas:
        print(message.format('carambolas'))
    if 'laranja' in frutas_favoritas:
        print(message.format('laranjas'))
    if 'maça' in frutas_favoritas:
        print(message.format('maças'))

def ola_admin_58():
    usernames = ['admin', 'mfelipe', 'rvitor', 'fsoares']
    for username in usernames:
        message = ''
        if username == 'admin':
            message = 'Olá, administrador. Gostaria de ver um relatório de status?'
        else:
            message = f'Olá, {username}.'

        print(message)

def sem_usuarios_59():
    usernames = ['admin', 'mfelipe', 'rvitor', 'fsoares']
    usernames = []
    if (usernames == []):
        print('Lista vazia.')
        print('É necessário encontrar alguns usuários.')
        return
    
    for username in usernames:
        message = ''
        if username == 'admin':
            message = 'Olá, administrador. Gostaria de ver um relatório de status?'
        else:
            message = f'Olá, {username}.'

        print(message)

def verificando_nomes_usuarios_510():
    current_users = [ 'mfelipe', 'mpereira', 'fvitor', 'rricardo', 'aneves' ]
    current_user_standardized = [user.lower() for user in current_users]
    new_users = [ 'rvitor', 'fsoares', 'meduarda', 'hannah1', 'mfelipe']
    for new_user in new_users:
        message = ''
        if new_user.lower() in current_users:
            message = f'O nome de usuário "{new_user}" está em uso. Escolha outro nome.'
        else:
            message = f'O nome de usuário "{new_user}" encontra-se disponível.'
        print(message)

def numeros_ordinais_511():
    numeros = list(range(0, 1_000_000))
    for numero in numeros:
        if numero > 3:
            print(f'{numero}th.')
        else:
            if numero == 1:
                print(f'{numero}st.')
            elif numero == 2:
                print(f'{numero}nd.')
            elif numero == 3:
                print(f'{numero}rd.')

# Funções criadas à título de teste de otimização
def numeros_ordinais_2_511():
    numeros = list(range(0, 1_000_000))
    for numero in numeros:
        if numero == 1:
            print(f'{numero}st.')
        elif numero == 2:
            print(f'{numero}nd.')
        elif numero == 3:
            print(f'{numero}rd.')
        else:
            print(f'{numero}th.')

# Funções criadas à título de teste de otimização
def numeros_ordinais_3_511():
    numeros = list(range(0, 1_000_000))
    lista_string = [(str(numero) + 'th\n') 
                    if numero > 3 
                    else (str(numero) + 'rd\n') if numero == 3 else (str(numero) + 'nd\n') if numero == 2 else (str(numero) + 'st\n')
                    for numero in numeros 
                    ]
    numeros_string = ''.join(lista_string)
    print(numeros_string)
# numeros_ordinais_2_511()

# Capítulo 6

def pessoa_61():
    pessoa = {
        'first_name': 'terry',
        'last_name': 'crews',
        'age': 55,
        'city': 'flint'
    }

    for key, value in pessoa.items():
        print(f'{key}: {value}.')
    
def numeros_favoritos_62():
    numeros_favoritos = {
        'julie': 51,
        'cabral': 157,
        'pedro': 171,
        'peter': 22,
        'ricardo': 1
    }
    
    for nome, numero_favorito in numeros_favoritos.items():
        print(f'O número favoritm o de {nome} é {numero_favorito}.')

def glossario_63():
    glossario = {
        'if': 'Estrutura condicional que permite que o bloco de código dentro de si seja compilado se sua condição for satisfeita.',
        'elif': 'Estrutura condicional complementar que é executada se a condição do bloco if não for satisfeita e a sua própria for.',
        'else': 'Estrutura condicional complementar que é executada '
            'quando nenhuma das condições das outras estruturas que a prescederam foram satisfeitas.',
        'for': 'Estrutura de repetição que itera sobre um tipo que representa um grupo, como listas, tuplas e conjuntos.',
        'while': 'Estrutura de repetição que repete determinado bloco de código enquanto determinada condição for verdadeira.',
        'function': 'Blocos de código reutilizáveis que são executados quando chamados. Podem receber parâmetros e retornar resultados.',
        'class': 'Estrutura que permite a criação de objetos complexos. '
            'São modelos para a criação de instâncias com atributos e métodos específicos.',
        'try-except': 'Estrutura utilizada para tratamento de exceções. '
            'O bloco `try` executa código que pode gerar uma exceção e o `except` trata a exceção capturada.',
        'list comprehension': 'Método conciso para criar listas, '
            'gerando novas listas aplicando uma expressão a cada item de uma sequência existente.',
        'lambda': 'Função anônima expressa em uma única linha, '
            'usada para funções simples, podendo receber qualquer número de argumentos, mas só pode ter uma expressão.',
    
    }
    print('Glossário\n')
    for palavra, significado in glossario.items():
        print(f'{palavra}:\n\t{significado}')

def glossario_64():
    # O objetivo deste exercício era alterar o exercício 63.
    pass

def rios_65():
    rios = {
        'nilo': 'egito',
        'amazonas': 'brasil',
        'yangtze': 'china'
    }
    for rio, pais in rios.items():
        print(f'O rio {rio.title()} atravessa o {pais.title()}')

def pesquisa_66():
    linguagens_favoritas = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        'phil': 'python',
    }

    pessoas_para_participar = [ 'roberto', 'josh', 'sarah', 'ricardo', 'phil']

    for pessoa in pessoas_para_participar:
        message = f'Por favor, {pessoa}, participe de nossa pesquisa.'
        if pessoa in linguagens_favoritas:
            message = f'Obrigado pela resposta, {pessoa.title()}.'
        
        print(message)

def pessoas_67():
    pessoa_1 = {
        'first_name': 'terry',
        'last_name': 'crews',
        'age': 55,
        'city': 'flint'
    }
    pessoa_2 = {
        'first_name': 'kazunori',
        'last_name': 'yamauchi',
        'age': 56,
        'city': 'kashiwa'
    }
    pessoa_3 = {
        'first_name': 'marie',
        'last_name': 'curie',
        'age': 77,
        'city': 'varsóvia'
    }

    people = [ pessoa_1, pessoa_2, pessoa_3 ]

    for pessoa in people:
        for key, value in pessoa.items():
            print(f'{key}: {str(value).title()}.')
        print()

def animais_estimacao_68():
    pet_1 = {
        'type': 'dog',
        'owner': 'matthews'
    }
    pet_2 = {
        'type': 'cat',
        'owner': 'rita'
        }
    pet_3 = {
        'type': 'horse',
        'owner': 'henrique'
    }

    pets = [ pet_1, pet_2, pet_3 ]
    message = ...
    for pet in pets:
        for key, value in pet.items():
            message = f'{key}: {value.title()}'
            print(message)
        print()

def lugares_favoritos_69():
    favorite_places = {
        'roberto': ['roma', 'noruega', 'paris'],
        'lucas': ['roma', 'saint tropez', 'provença'],
        'julia': ['alpes italianos', 'lago de garda', 'londres'],
    }

    for name, places in favorite_places.items():
        print(f"{name.title()}'s favorite places are: ")
        for place in places:
            print(f'\t- {place.title()};')

# Capítulo 7
            
def aluguel_carro_71():
    tipo_carro = input('Qual tipo de carro você gostaria de alguar?\n')
    print(f'Vejamos se consigo encontrar um {tipo_carro} para você.')

def reservas_restaurante_72():
    number_of_seats = input('Quantos lugares em uma mesa você precisa?\n')
    number_of_seats = int(number_of_seats)
    message = 'Sua mesa já está disponível.'
    if number_of_seats > 8:
        message = 'Será necessário aguardar por uma mesa.'
    print(message)

def multiplos_dez_73():
    numero = input('Entre com um número: ')
    numero = int(numero)
    message = 'Não é múltiplo de 10.'
    if numero % 10 == 0:
        message = 'É múltiplo de 10.'
    print(message)

def ingredientes_pizza_74():
    quit = False
    while (quit == False):
        entrance = input('Entre com um ingrediente da pizza. ')
        if entrance == 'quit':
            quit = True
            continue
        print(f'{entrance.title()} está sendo adicionado à pizza.')

def ingressos_cinema_75():
    
    keep = True
    while keep:
        entrance = input('Entre com sua idade(type "quit" to stop): ')

        if entrance == 'quit':
            keep = False
            continue

        age = int(entrance)
        ticket_price = ...
        if age < 3:
            ticket_price = 0.0
        elif 3 <= age <= 12:
            ticket_price = 10.0
        elif age > 12:
            ticket_price = 15.0
        
        message = f'O ingresso irá custar US$ {ticket_price:.2f}'
        print(message)

def tres_saidas_76():
    active = True
    while active:
        entrance = input('Entre com sua idade(type "quit" to stop): ')

        if entrance == 'quit':
            active = False
            continue

        age = int(entrance)
        ticket_price = ...
        if age < 3:
            ticket_price = 0.0
        elif 3 <= age <= 12:
            ticket_price = 10.0
        elif age > 12:
            ticket_price = 15.0
        
        message = f'O ingresso irá custar US$ {ticket_price:.2f}'
        print(message)

def tres_saidas_2_76():
    
    while True:
        entrance = input('Entre com sua idade(type "quit" to stop): ')

        if entrance == 'quit':
            break

        age = int(entrance)
        ticket_price = ...
        if age < 3:
            ticket_price = 0.0
        elif 3 <= age <= 12:
            ticket_price = 10.0
        elif age > 12:
            ticket_price = 15.0
        
        message = f'O ingresso irá custar US$ {ticket_price:.2f}'
        print(message)

def infinito_77():
    # O seguinte exercício exige que um loop infinito seja criado, portanto, trata-se de um erro intencional.
    while True:
        input('Este é um loop infinito, digite qualquer coisa para continuar.(ctrl + c para finalizar o programa) ')

def lanchonete_78():
    sandwich_orders = [ 
        'sanduíche natural de atum simples',
        'sanduíche de frango e cottage',
        'sanduíche gelado de atum',
        'sanduiche de ovo',
     ]
    
    finished_sandwiches = []

    for sandwich in sandwich_orders[:]:
        print(f'Seu {sandwich} está pronto.')
        finished_sandwiches.append(sandwich_orders.pop(0))

    print()
    for sandwich in finished_sandwiches:
        print(f'{finished_sandwiches.index(sandwich) + 1} - {sandwich}')

def lanchonete_2_78():
    sandwich_orders = [ 
        'sanduíche natural de atum simples',
        'sanduíche de frango e cottage',
        'sanduíche gelado de atum',
        'sanduiche de ovo',
     ]
    
    finished_sandwiches = []

    while sandwich_orders:
        sandwich = sandwich_orders.pop(0)
        print(f'Seu {sandwich} está pronto.')
        finished_sandwiches.append(sandwich)

    print()
    for sandwich in finished_sandwiches:
        print(f'{finished_sandwiches.index(sandwich) + 1} - {sandwich.title()}')

def sem_pastrami_79():
    sandwich_orders = [ 
        'sanduíche de pastrami', 
        'sanduíche natural de atum simples',
        'sanduíche de pastrami', 
        'sanduíche de frango e cottage',
        'sanduíche de pastrami', 
        'sanduíche gelado de atum',
        'sanduíche de pastrami', 
        'sanduíche de ovo',
     ]
    
    print('Lamentamos informar que a lanchonete encontra-se sem pastrami no momento.')

    while 'sanduíche de pastrami' in sandwich_orders:
        sandwich_orders.remove('sanduíche de pastrami')

    finished_sandwiches = []

    while sandwich_orders:
        sandwich = sandwich_orders.pop(0)
        print(f'Seu {sandwich} está pronto.')
        finished_sandwiches.append(sandwich)

    print()
    for sandwich in finished_sandwiches:
        print(f'{finished_sandwiches.index(sandwich) + 1} - {sandwich.title()}')

def ferias_tao_sonhadas_710():
    dream_vacation = {}
    while True:
        name = input('Entre com seu nome. ')
        if name == 'quit':
            break;
        place = input('Se pudesse visitar qualquer lugar do mundo, para onde iria? ')
        if place == 'quit':
            break;
        dream_vacation[name] = place

    for name, place in dream_vacation.items():
        print(f'{name.title()} iria para {place.title()}.')





ferias_tao_sonhadas_710()