import calendar

year = int(input('Enter Year: '))
month = int(input('Enter Month: '))
print(calendar.month_name[month]) # Get the full name of the month

print(calendar.calendar(year, 3, 1, 8)) # Display the calendar for the entire year with a width of 3, 1 month per line, and 8 lines per page