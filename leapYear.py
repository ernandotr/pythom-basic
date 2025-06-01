import calendar

current_year = calendar.datetime.date.today().year  # Get the current year

userYear = input('Enter Year: ')  # Prompt user for a year
year = int(userYear) if userYear else current_year  # Use current year if no input is given

print(calendar.isleap(year)) # Check if the year is a leap year
