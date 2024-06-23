# Prompt the user to enter a year
year = int(input("Enter the year: "))

# Check if the given year is a leap year
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
# If a year is evenly divisible by 4 means having no remainder then go to next step. If it is not divisible by 4. It is not a leap year. For example: 1997 is not a leap year.
# If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year. If a year is divisible by both 4 and 100, go to next step.
# If a year is divisible by 100, but not by 400. For example: 1900, then it is not a leap year. If a year is divisible by both, then it is a leap year. So 2000 is a leap year.
    print(f"{year} is a leap year, it is 366 days.")
else:
    # If the year doesn't meet the criteria for a leap year, it's not a leap year
    print(f"{year} is not a leap year, it is 365 days.")
