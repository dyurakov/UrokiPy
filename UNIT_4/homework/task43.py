# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

import datetime

free_dates = []

for month in range(1, 13):
    for day in range(1, 31+1):
        try:
            date = datetime.date(2023, month, day)
        except:
            continue
        if date.weekday() == 3 and day > 14 and day < 22:
            free_dates.append(date)

for date in free_dates:
    print(date)