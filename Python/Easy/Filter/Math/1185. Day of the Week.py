from datetime import datetime


def dayOfTheWeek(day: int, month: int, year: int) -> str:
    date_obj = datetime(year, month, day)
    return date_obj.strftime("%A")


day = 31
month = 8
year = 2019

print(dayOfTheWeek(day, month, year))
