# Identify the day number using date time module
import datetime
day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))

date=datetime.date(year,month,day)
day_of_year=date.timetuple().tm_yday
print("Day number is:",day_of_year)