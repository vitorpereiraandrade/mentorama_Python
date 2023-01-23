import datetime

hoje = datetime.date.today()
print(f'Hoje: {hoje}')

antes = hoje - datetime.timedelta(days=2)
print(f'Antes de ontem: {antes}')

depois = hoje + datetime.timedelta(days=2)
print(f'Depois de amanha: {depois}')

