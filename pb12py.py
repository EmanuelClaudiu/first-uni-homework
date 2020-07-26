def is_bisect(year):
    if year % 4 == 0:
        return 1
    else:
        return 0


import datetime
from datetime import date, timedelta

current_date = date.today()

current_day = current_date.day
current_month = current_date.month
current_year = current_date.year

year = 0
month = 0
day = 0

year = int(input('What year were you born in? '))
month = int(input('What about the month? '))
day = int(input('But which day? '))

def is_bisect(year):
    if year % 4 == 0:
        return 1
    else:
        return 0

def how_much_until_the_year_ends(day, month, year):
    days = [0 , 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    s = 0

    if is_bisect(year):
        days[2] = 29

    for i in range(day, days[month]):
        s += 1

    for i in range(month, 12):
        s += days[i]

    return s-1

def how_many_days_passed(day, month, year):
    days = [0 , 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    s = 0

    if is_bisect(year):
        days[2] = 29

    for i in range(1, month):
        s += days[i]
    
    for i in range(1, day):
        s += 1

    return s

s = 0

#s += how_much_until_the_year_ends(day, month, year)
#s += how_many_days_passed(current_day, current_month, current_year)

if (year == current_year):
    s = how_many_days_passed(current_day, current_month, current_year) - how_many_days_passed(day, month, year) 
else:
    s += how_much_until_the_year_ends(day, month, year)
    s += how_many_days_passed(current_day, current_month, current_year)
    s += 2

for i in range(year+1, current_year):
    if (is_bisect(i)):
        s += 366
    else:
        s += 365

print ("You've lived" ,s, "days")