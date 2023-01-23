try:
    nome = 'Vitor Pereira Andrade'
    print(nome)
except SyntaxError:
    print('Erro de Sintaxe')
finally:
    print(f'Olá {nome}')