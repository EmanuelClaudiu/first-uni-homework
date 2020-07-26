def is_bisect(year):
    if year % 4 == 0:
        return 1
    else:
        return 0

year = 0
day_number = 0

year = int(input('What is the year: '))
day_number = int(input('What is the day number: '))

day = 0

if (is_bisect(year)):
    if (day_number < 31):
        day = day_number
        month = 'January'
    if (day_number >= 32 and day_number <= 60):
        day = day_number - 31
        month ='February'
    if (day_number >= 61 and day_number <= 91):
        day = day_number - 60
        month = 'March'
    if (day_number >= 92 and day_number <= 121):
        day = day_number - 91
        month = 'April'
    if (day_number >= 122 and day_number <= 152):
        day = day_number - 121
        month = 'May'
    if (day_number >= 153 and day_number <= 182):
        day = day_number - 152
        month = 'June'
    if (day_number >= 183 and day_number <= 213):
        day = day_number - 182
        month = 'July'
    if (day_number >= 214 and day_number <= 244):
        day = day_number - 213
        month = 'August'
    if (day_number >= 245 and day_number <= 274):
        day = day_number - 244
        month = 'September'
    if (day_number >= 275 and day_number <= 305):
        day = day_number - 274
        month = 'October'
    if (day_number >= 306 and day_number <= 335):
        day = day_number - 305
        month = 'November'
    if (day_number >= 336 and day_number <= 366):
        day = day_number - 335
        month = 'December'
else:
    if (day_number < 31):
        day = day_number
        month = 'January'
    if (day_number >= 32 and day_number <= 59):
        day = day_number - 31
        month ='February'
    if (day_number >= 60 and day_number <= 90):
        day = day_number - 59
        month = 'March'
    if (day_number >= 91 and day_number <= 120):
        day = day_number - 90
        month = 'April'
    if (day_number >= 121 and day_number <= 151):
        day = day_number - 120
        month = 'May'
    if (day_number >= 152 and day_number <= 181):
        day = day_number - 151
        month = 'June'
    if (day_number >= 182 and day_number <= 212):
        day = day_number - 181
        month = 'July'
    if (day_number >= 213 and day_number <= 243):
        day = day_number - 212
        month = 'August'
    if (day_number >= 244 and day_number <= 273):
        day = day_number - 243
        month = 'September'
    if (day_number >= 274 and day_number <= 304):
        day = day_number - 273
        month = 'October'
    if (day_number >= 305 and day_number <= 334):
        day = day_number - 304
        month = 'November'
    if (day_number >= 335 and day_number <= 365):
        day = day_number - 334
        month = 'December'

print (day, month, year)