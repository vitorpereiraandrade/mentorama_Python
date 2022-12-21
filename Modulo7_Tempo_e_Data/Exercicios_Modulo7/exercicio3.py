import time
from time import perf_counter

start = time.time()
star2 = perf_counter()

def hello():
    for h in range(5):
        time.sleep(3)
        print('Ola mundo !!!')
hello()

end = time.time()
end2 = perf_counter()

print(f'Tempo de processamento foi de {end - start:.5f}')
print(f'Tempo de processamento foi de {end2 - star2:.5f}')