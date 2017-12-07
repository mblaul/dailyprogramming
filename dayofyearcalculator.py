## author Matt Blail
## 12/6/2017

import calendar

c = calendar.TextCalendar([])

print(c.monthdatescalendar(2017,11))




# def is_leapyear(year):
#     if(int(year) % 4 == 0):
#         if(int(year) % 100 == 0):
#             if(int(year) % 400 == 0):
#                 return True;
#             return False;
#         return True;
#
# def main():
#
#     date = "400 10 30"
#
#     date = date.split()
#     year = date[0]
#     month = date[1]
#     day = date[2]
#
#     print(year,month,day)
#
#     if(is_leapyear(year) == True):
#         print(year +" is a leap year")
#     else:
#         print(year +" is NOT leap year")
#
# main()
## Resources used:
## https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
