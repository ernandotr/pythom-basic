import calendar

year = int(input('Enter Year: '))
month = int(input('Enter Month: '))

print(calendar.monthcalendar(year, month))  # Display the month's calendar as a matrix