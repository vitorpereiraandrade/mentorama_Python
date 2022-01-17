import math
from typing import List, Union

quantidade_pessoas = []
mulher = []
idade = []
media_acima = []

while True:
    entrada = str(input('Deseja fazer o cadastro? S para sim e N para nao: ')).upper()
    if entrada != 'S':
        break
    else:
        cadastro_pessoas = dict(Nome=input('Digite nome: ').upper(),
                                Sexo=input('Digite sexo M Masculino e F Feminino: ').upper(),
                                Idade=int(input('Digite a idade: ')))
        quantidade_pessoas.append(cadastro_pessoas)
        idade.append(cadastro_pessoas['Idade'])
        if cadastro_pessoas['Sexo'] == 'F':
            mulher.append(cadastro_pessoas['Nome'])

idade_media = (sum(idade) / len(quantidade_pessoas))
for i in quantidade_pessoas:
    if i['Idade'] > idade_media:
        media_acima.append(i['Nome'])


print(f'Foram cadastradas {len(quantidade_pessoas)} pessoas no total')
print(f'A idade média das pessoas cadastradas é de: {idade_media:.0f} anos')
print(f'As mulheres cadastradas são: {mulher}')
print(f'As pessoas cadastradas acima da média de {idade_media:.0f} anos são: {media_acima}')



### TESTE GITHUB