import calendar

year = int(input('Enter Year: '))  # Prompt user for a year
month = int(input('Enter Month: '))  # Prompt user for a month
print(calendar.month(year, month))  # Display the month's calendar

print(calendar.monthrange(year, month)) # Get the first weekday and number of days in the month
print(calendar.weekday(year, month, 1)) # Get the weekday of the first day of the month
print(calendar.firstweekday()) # Get the first weekday of the calendar