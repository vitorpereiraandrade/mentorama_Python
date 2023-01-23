import random
import time

# Vamos ver um exemplo de como calcular tempo de execução de um programa que gera 1000 números aleatórios:

inicio = time.time()
for x in range(1000):
    numeros = random.randint(1, 1000)
fim = time.time()
print(f"Tempo de execução: {fim - inicio}")

# Vamos agora somar todos os números aleatórios e mostrar na telas os números e as somas:

soma = 0

inicio = time.time()
for x in range(1000):
    numeros = random.randint(1, 1000)
    soma += numeros
fim = time.time()

print(f"Tempo de execução: {fim - inicio}")

# Agora vamos ver o tempo de execução depois de adicionar uma linha que printa os números gerados dentro da repetição:

inicio = time.time()
for x in range(1000):
    numeros = random.randint(1, 1000)
    print(numeros)
fim = time.time()

print(f"Tempo de execução: {fim - inicio}")


# E se aumentarmos de 1000 números aleatórios para 1000000? Como ficará o tempo de execução?

inicio = time.time()
for x in range(1000000):
    numeros = random.randint(1, 1000000)

fim = time.time()
print(f"Tempo de execução: {fim - inicio}")

# Vamos então utilizar o conceito de threads neste último programa. Será que o desempenho melhora? Em programação paralela
# o que nos permite executar mais de uma linha de código de uma vez são as Threads pois elas compartilham a área de memória com outras linhas.


from threading import Thread


# primeiro vamos criar uma função que implementa o código anterior

def geraAleatorio(qtd):
    for x in range(qtd):
        numeros = random.randint(1, 1000000)


inicio = time.time()
# cria o objeto thread t1 que executará a função acima
t1 = Thread(target=geraAleatorio, args=[1000000])

# inicia a thread
t1.run()
fim = time.time()

print(f"Tempo de execução: {fim - inicio}")



