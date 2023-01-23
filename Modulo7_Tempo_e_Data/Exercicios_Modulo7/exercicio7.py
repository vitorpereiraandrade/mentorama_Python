from datetime import timedelta, date
hoje = date.today()
intervalo = timedelta(8)
passado = hoje - intervalo
print(f'Data Atual: {hoje}\nData esperada: {passado}')