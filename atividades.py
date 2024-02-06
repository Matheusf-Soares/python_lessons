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

foods_412()

