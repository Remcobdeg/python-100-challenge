import datetime as dt

now = dt.datetime.now() #current date and time
print(now) #2024-10-11 20:34:59.481391
print(type(now)) #<class 'datetime.datetime'>
print(now.year) #2024
print(type(now.year)) #<class 'int'>

#create date
date_of_year = dt.datetime(day=16, month=6, year=1988)