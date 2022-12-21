import time
from threading import Timer

help(time.gmtime())

# Definindo uma época
print(time.gmtime(0))

# Tempo em segundos que se passaram desde uma época sendo seconds, um número float
seconds = time.time()
print(f'Segundos desde a época: {seconds}')

# A  função leva segundos passados desde a época como um argumento e retorna uma string representando a hora local
# Segunods passados desde a época foram definidos anteriormente
local_time = time.ctime(seconds)
print(f'Tempo local: {local_time}')

# Imprime o tempo no momento
print(f'Tempo local: {time.asctime()}')

# Imprime dados de tempo derivados sintaxe de struct
print(time.localtime())

# Cria um objeto Localtime e imprime o valor na posição desejada
a = time.localtime()
print(a[0])
print(a[3:6])

# O módulo de tempo tem uma função strftime que funciona praticamente da mesma maneira que a versão datetime
# A diferença está principalmente no que ele aceita como entrada: uma tupla ou um objeto struct_time,
# quando você chama time.gmtime() ou time.localtime().
print(time.strftime("%Y-%m-%d-%H.%M.%S´", time.localtime()))

# Criando um delay de tempo: a função atrasa a execução do thread atual por um determinado número de segundos
time.sleep(3)  # Sleep for 3 seconds
print('Isso é impresso depois de 3 segundos')

print("Isso é impresso imediatamente")
time.sleep(5)
print('Isso é impresso depois de 5 segundos')


# Podemos criar um timer para que a instrução seja executadfa em um tempo programado
def hello():
    print('Hello world !!!!!')


t = Timer(5, hello)
t.start()  # depois de 5 segundos

# Calculando o tempo de execução de uma instrução
start_exec = time.time()


def hello():
    time.sleep(5)
    print("Hello World !!!!!")


hello()
end_exec = time.time()
print(f'O tempo de execução total corresponde a: {end_exec - start_exec}')

print('')

# USANDO A FUNCAO perf_counter()
# O objetivo da função é retornar o valor tipo float de tempo em segundos
# perf_counter() fornece um valor mais preciso do que a função time.clock() descontinuada no Python 3.8
# Podemos calcular float e integer, ambos os valores de tempo em segundos e nanossegundos.
# "O programa abaixo solicita ao usuário dois números inteiros a serem inseridos em uma mesma linha. Ao entrar no loop,
# o programa solicita um novo valor. Se esse 3º valor for divisível pelo 2º valor, logo o resto será zero e último número inserido será impresso.
# O programa irá fazer esse loop a quantidade de vezes correspondente ao primeiro valor inserido."

# Python program to show time by perf_counter()
from time import perf_counter

# entrada dos numeros inteiros a partir do usuario, duas entradas em uma unica linha
print("Entre com dois valores inteiros")
n, m = map(int, input().split())

# Start the stopwatch / counter
t1_start = perf_counter()

for i in range(n):
    print('Insira um valor inteiro')
    t = int(input()) # usuario deu entrada n vezes
    if t % m == 0:
        print(t)

# Stop the stopwatch / counter

t1_stop = perf_counter()

print(f'Tempo decorrido: {t1_stop, t1_start}')
print(f'Tempo decorrido durante todo o programa, em segundos: {t1_stop-t1_start}')
