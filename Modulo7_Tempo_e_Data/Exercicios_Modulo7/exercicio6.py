from datetime import datetime

data = '2021-01-01-13:53:00'
d = datetime.strptime(data, '%Y-%m-%d-%H:%M:%S')
print(d)