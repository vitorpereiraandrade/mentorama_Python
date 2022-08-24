# Tratando exceções FileNotFoundError

try:
    f = open('texto.txt', 'r')
except FileNotFoundError:
    print('Arquivo não encontrado')
    print('Criar um arquivo')
except:
    print('Ocorreu um erro')

print('')
# Tratando exceçõs de NameErros

var5 = 10
try:
    print(var5)
except NameError:
    print('Nome não definido!')
else:
    print('Tente novamente')
finally:
    print('Programa Finalizado')

print('')


# Um exemplo um pouco mais complexo com iteração e biblioteca Math
import math

number_list = [10, -5, 1.2, 'aplle']

for number in number_list:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print('Fatorial não é suportado pela tipo de entrada recebido')
    except ValueError:
        print(f'Fatorial aceita somente valores inteiros positivos e {number} não é um inteiro positivo ')
    else:
        print(f'O fatorial de {number} é {number_factorial}')
    finally:
        print('Libere todos os recursos em uso')





