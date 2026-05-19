import datetime

year = int(input("Enter year: "))

month = 1
while month <= 12:
    # Print month name
    if month == 1:
        print("\nJanuary", year)
    elif month == 2:
        print("\nFebruary", year)
    elif month == 3:
        print("\nMarch", year)
    elif month == 4:
        print("\nApril", year)
    elif month == 5:
        print("\nMay", year)
    elif month == 6:
        print("\nJune", year)
    elif month == 7:
        print("\nJuly", year)
    elif month == 8:
        print("\nAugust", year)
    elif month == 9:
        print("\nSeptember", year)
    elif month == 10:
        print("\nOctober", year)
    elif month == 11:
        print("\nNovember", year)
    elif month == 12:
        print("\nDecember", year)

    # Print day headers
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Find the weekday of first day (0=Monday)
    first_day = datetime.date(year, month, 1).weekday()
    
    # Print leading spaces
    day = 0
    while day < first_day:
        print("    ", end="")
        day += 1

    # Find number of days in month
    if month == 12:
        days_in_month = (datetime.date(year+1, 1, 1) - datetime.date(year, month, 1)).days
    else:
        days_in_month = (datetime.date(year, month+1, 1) - datetime.date(year, month, 1)).days

    # Print all days
    day = 1
    count = first_day
    while day <= days_in_month:
        print(f"{day:>3} ", end="")
        day += 1
        count += 1
        if count % 7 == 0:
            print()
    print("\n")
    month += 1
