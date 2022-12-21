import datetime

day = datetime.timedelta(days=1)
start = datetime.date(87, 10, 16)
end = datetime.date(87, 10 , 25)
for i in range((end - start).days):
    print(start + i*day)