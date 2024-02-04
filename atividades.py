# Capítulo 3

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

propria_lista_33()