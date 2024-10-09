from datetime import datetime, timedelta
#primeiro
data_atual = datetime.now()
date_two_days = data_atual + timedelta(2)
print(data_atual)
print(date_two_days)

#segundo
data_hj = datetime.now()
print(data_hj.date())

#terceiro
dict = {'m1':{'m2': 'Olá mundo'}}
print(dict['m1']['m2'])


