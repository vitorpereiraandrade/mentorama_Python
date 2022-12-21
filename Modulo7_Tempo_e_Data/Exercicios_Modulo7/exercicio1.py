import time
'a)'
print(time.gmtime(0))

'b)'
segundos = time.time()
print(f'Segundos desde a época: {segundos}')

'c)'
print(f'Tempo no momento atual: {time.asctime()}')

'd)'
a = time.localtime()
print(f'Horas {a[3]}, Minutos {a[4]}, Segundos {a[5]}')

'e)'
verao = time.localtime()
print(f'Horario verao {verao[8]}')

