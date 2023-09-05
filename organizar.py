#Aula python 08/28/2023
'''
Exercicio 27: CÃ¡lculos com kwargs
Crie uma funÃ§Ã£o que aceite argumentos nomeados (**kwargs) representando 
valores e operaÃ§Ãµes matemÃ¡ticas, e retorne o resultado dessas operaÃ§Ãµes.
'''

#DefiniÃ§Ã£o de funÃ§Ã£o

def calcular(**kwargs):
    valor = kwargs['valor']
    operacoes = kwargs['operacoes']
    resultado = valor
    for operacao in operacoes:
        if operacao[0] == '+':
            resultado += operacao[1]
        elif operacao[0] == '-':
            resultado -= operacao[1]
        elif operacao[0] == '*':
            resultado *= operacao[1]
        elif operacao[0] == '/':
            resultado /= operacao[1]
    return resultado

valor = float(input("Digite um valor: "))
operacoes = []
while True:
    op = input("Digite a operaÃ§Ã£o (+, -, *, /) e o valor separados por espaÃ§o (ou 'fim' para parar): ")
    if op == 'fim':
        break
    operacao, valor_op = op.split()
    operacoes.append((operacao, float(valor_op)))

resultado = calcular(valor=valor, operacoes=operacoes)
print("Resultado:", resultado)

'''
Exercicio 28: CÃ¡lculos com kwargs
FunÃ§Ã£o com kwargs para converter moedas
Crie uma funÃ§Ã£o que aceite um valor em dÃ³lares e uma taxa de conversÃ£o como 
argumentos nomeados (**kwargs) e retorne o valor convertido para a moeda especificada.
'''

#DefiniÃ§Ã£o de funÃ§Ã£o

def converter_moeda(**kwargs):
    valor_dolares = kwargs.get('valor_dolares', 0)
    taxa = kwargs.get('taxa', 1)
    valor_convertido = valor_dolares * taxa
    return valor_convertido

valor = float(input("Digite o valor em dÃ³lares: "))
taxa = float(input("Digite a taxa de conversÃ£o: "))
valor_convertido = converter_moeda(valor_dolares=valor, taxa=taxa)
print(f"Valor convertido: {valor_convertido:.2f}")


'''
Exercicio 29: FunÃ§Ã£o com args para verificar nÃºmeros primos
Crie uma funÃ§Ã£o que aceite nÃºmeros como argumentos *args e retorne 
uma lista contendo os nÃºmeros primos dessa lista.

'''

#DefiniÃ§Ã£o de funÃ§Ãµes

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos(*args):
    primos = [num for num in args if eh_primo(num)]
    return primos

numeros = [int(x) for x in input("Digite nÃºmeros separados por espaÃ§o: ").split()]
primos_encontrados = encontrar_primos(*numeros)
print("NÃºmeros primos:", primos_encontrados)


'''
Exercicio 30: FunÃ§Ã£o com args para verificar nÃºmeros primos
Crie uma funÃ§Ã£o que aceite nÃºmeros como argumentos *args e retorne 
uma lista contendo os nÃºmeros primos dessa lista.

'''

#DefiniÃ§Ã£o de funÃ§Ãµes

def calcular_juros_compostos(**kwargs):
    principal = kwargs.get('principal', 0)
    taxa_juros = kwargs.get('taxa_juros', 0)
    periodo = kwargs.get('periodo', 0)
    montante = principal * (1 + (taxa_juros / 100)) ** periodo
    return montante

principal = float(input("Digite o valor principal: "))
taxa = float(input("Digite a taxa de juros (em %): "))
periodo = int(input("Digite o perÃ­odo (em anos): "))
montante_final = calcular_juros_compostos(principal=principal, taxa_juros=taxa, periodo=periodo)
print(f"Montante final: R$ {montante_final:.2f}")

'''
EXERCICIOS ENVOLVENDO DICIONARIO
'''

'''
Exercicio 31 - Enunciado: Crie um dicionÃ¡rio vazio e imprima-o
'''

dictio = {}
print(dictio)

'''
ExercÃ­cio 32 - Enunciado: Crie um dicionÃ¡rio com trÃªs pares chave-valor 
representando nomes de frutas e suas quantidades. Imprima o dicionÃ¡rio.
'''

frutas = {'maca': 5, 'banana': 3, 'laranja': 7}
print(frutas)

'''
ExercÃ­cio 33 - Enunciado: Adicione uma nova fruta ao dicionÃ¡rio do exercÃ­cio 32
com sua respectiva quantidade. Imprima o dicionÃ¡rio atualizado.
'''

frutas['uva'] = 9
print(frutas)

'''
ExercÃ­cio 34 - Enunciado: Dado um dicionÃ¡rio de notas dos alunos, 
calcule a mÃ©dia das notas e imprima o resultado.
'''

notas = {'Alice': 85, 'Bob': 92, 'Carol': 78}
media = sum(notas.values()) / len(notas)
print(f"A mÃ©dia das notas Ã©: {media:.2f}")

'''
ExercÃ­cio 35 - Enunciado: Crie um dicionÃ¡rio de palavras e suas traduÃ§Ãµes 
em outro idioma. PeÃ§a ao usuÃ¡rio para digitar uma palavra e retorne 
a traduÃ§Ã£o correspondente, se existir.
'''

translations = {'hello': 'olÃ¡', 'dog': 'cÃ£o', 'cat': 'gato'}
palavra = input("Digite uma palavra: ")
translation = translations.get(palavra, "TraduÃ§Ã£o nÃ£o encontrada")
print(translation)

'''
ExercÃ­cio 36 - Enunciado: Crie um dicionÃ¡rio com nomes de cidades 
como keys e suas populaÃ§Ãµes como valores. PeÃ§a ao usuÃ¡rio para 
digitar uma cidade e mostre a populaÃ§Ã£o correspondente.
'''

cidades = {'New York': 8623000, 'Los Angeles': 3990000, 'Chicago': 2716000}
cidade = input("Digite o nome da cidade: ")
populacao = cidades.get(cidade, "Cidade nÃ£o encontrada")
print(f"A populaÃ§Ã£o de {cidade} Ã© {populacao}")

'''
ExercÃ­cio 37 - Enunciado: Crie um dicionÃ¡rio com nomes de produtos e
seus preÃ§os. Calcule o valor total de uma lista de compras fornecida pelo usuÃ¡rio.
'''

produtos = {'maca': 1.25, 'banana': 0.75, 'laranja': 0.90}
shopping_list = input("Digite os produtos da lista (separados por vÃ­rgula): ").split(',')
total_cost = sum(produtos[item] for item in shopping_list if item in produtos)
print(f"O custo total Ã©: R${total_cost:.2f}")


'''
ExercÃ­cio 38 - Enunciado: Crie um programa que simule um dicionÃ¡rio de contatos. 
Permita ao usuÃ¡rio adicionar, remover e buscar contatos pelo nome.
'''

contatos = {}

while True:
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Sair")
    choice = int(input("choice uma opÃ§Ã£o: "))
    
    if choice == 1:
        nome = input("Digite o nome do contato: ")
        numero = input("Digite o nÃºmero do contato: ")
        contatos[nome] = numero
    elif choice == 2:
        nome = input("Digite o nome do contato a ser removido: ")
        if nome in contatos:
            del contatos[nome]
            print(f"Contato {nome} removido.")
        else:
            print("Contato nÃ£o encontrado.")
    elif choice == 3:
        nome = input("Digite o nome do contato a ser buscado: ")
        numero = contatos.get(nome, "Contato nÃ£o encontrado")
        print(f"NÃºmero de {nome}: {numero}")
    elif choice == 4:
        break