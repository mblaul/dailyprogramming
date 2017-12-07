## author Matt Blail
## 12/6/2017

## Script to calculate the day of the week.
## Could be done in a more verbose way by using Zeller's Rule:
## https://en.wikipedia.org/wiki/Zeller's_congruence

import calendar
calendar.setfirstweekday(calendar.SUNDAY)

dates = ["2017 10 30",
        "2016 2 29",
        "2015 2 28",
        "29 4 12",
        "570 11 30",
        "1066 9 25",
        "1776 7 4",
        "1933 1 30",
        "1953 3 6",
        "2100 1 9",
        "2202 12 15",
        "7032 3 26"
        ]

for x in dates:
    print(x)

    x = x.split()
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])

    print(calendar.day_name[calendar.weekday(year,month,day)])
    print("-------------")
