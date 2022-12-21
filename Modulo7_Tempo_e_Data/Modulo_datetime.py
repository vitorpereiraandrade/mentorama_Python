import datetime


# Datetime é um módulo que fornece as classes para tratamento de datas, horas, minutos, segundos etc

# Armazenando e atribuindo valores

# armazenando uma data específica
umadata = datetime.date(2021, 2, 8)
print(umadata.year)
print(umadata.month)

# atribui valores a datatime
print(datetime.datetime(2021, 1, 2, 4, 20, 34, 565)) # ano, mes, dia, horas, min, seg e mile.

# armazenando a data de hoje
hoje = datetime.date.today()
# imprimindo datas
print(hoje.day)
print(hoje.weekday()) # segunda feira = 0 e domingo = 6
print(hoje.isoweekday()) # segunda = 1 e domingo = 7

# atribuindo a data e o tempo atual ao objeto y
y = datetime.datetime.now()
print(y.year)
print(y.month)
print(y.day)

# Imprimindo uma lista de datas no intervalo entre duas datas
#  * A função Python timedelta () está presente na biblioteca datetime, que geralmente é usada para calcular diferenças em
# datas e também pode ser usada para manipulações de datas em Pytho
# * É uma das maneiras mais fáceis de realizar manipulações de datas."

# Definindo o tamanho de cado passo em dias
day_delta = datetime.timedelta(days=1) # dia a dia,  se for a cada 2 dias ficaria (days=2), a cada 3 dias (days = 3)

start_date = datetime.date.today()
end_date = start_date + 5*day_delta # a cada um dia 5 vezes

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)

# Calculando a diferença entre dias
b1 = datetime.timedelta(days=25) # dia 25
b2 = datetime.timedelta(days=15) # dia 15
b3 = b2-b1
print(b3)
print(type(b3))

# Calculando a diferença entre dias entre uma data especifica e a data atual
from datetime import datetime, timedelta

now = datetime.now()
then = datetime(2019, 5, 23)
delta = now-then
print(delta)

# Calculando a diferença entre ontem e amanhã
import datetime

today = datetime.date.today()
print(f'Today: {today}')

yesterday = today - datetime.timedelta(days=1) # 1 dia de hoje menos 1 dia
print(f'Yesterday: {yesterday}')

tomorrow = today + datetime.timedelta(days=1) # 1 dia de hoje + 1 dia
print(f'Tomorrow: {tomorrow}')

print(f'Time between tomorrow and yesterday: {tomorrow - yesterday}') # intervalo de 2 dias

# Convertendo Strings no formato data e tempo
from datetime import datetime, timedelta

texto = '2021-02-08'
y = datetime.strptime(texto, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)








