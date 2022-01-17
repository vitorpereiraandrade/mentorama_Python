# Dicionarios sao escritos com chaves e suportam varios tipos de dados, com a sintaxe:
func = {'matricula':123, 'nome':'Jose', 'idade':20, 'salario': 9200.45}
print(func)
vazio = {} # Criacao de um dicionario vazio
print(type(func))

# Inicializa um dicionario vazio
dicionario = dict()
print(dicionario)

# Definindo um dicionario:
# Perceba que o valor de ano é sobrescrito
dicionario = {
    'brand':'Fiat',
    'model':'Toro',
    'electric': False,
    'Year': 2020,
    'Year': 2019,
    'Colors':['red', 'white', 'blue']
}
print(dicionario)

# Vamos imprimir a marca do carro
print(dicionario['brand'])

# Criacao e manipulacao de dicionarios
dados = {'nome':'Ricardo', 'visitas':25}
print(dados)

#Impressao do valor atribuido a nome
print(dados['nome'])

#Incrementando a visita
dados['visitas'] += 1
print(dados['visitas'])

# Verifica se existe um valor para nome em nosso dicionario
print('nome' in dados)
print(dados.keys())
print(dados.values())
print(dados.items())



