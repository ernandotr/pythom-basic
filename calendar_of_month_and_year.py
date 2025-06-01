import calendar
# Display the calendar for a specific month and year
year = int(input('Enter Year:'))
month = int(input('Enter Month:'))
print(calendar.month(year, month, w = 3)) # Display the month's calendar with a width of 3