import calendar

def printcalendar(year):
    print(calendar.calendar(year))

year = int(input("Enter a year : "))
printcalendar(year)