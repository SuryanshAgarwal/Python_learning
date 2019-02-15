import datetime

print(datetime.date.today())

today = datetime.date.today()
preDate = datetime.date(2010,1,25)
diff = today-preDate
print(diff.days)

if preDate < today:
    print('condition checked :')
    preDate = preDate.replace(year=today.year+1) 
print(preDate)
print('UTC now: ',datetime.time())