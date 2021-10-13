# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("What month? ").lower()
day = int(input("What day? "))

season = ""
if month in ("jan", "feb"):
    season = "winter"
elif month == "mar":
    if day in range(1, 20):
        season = "winter"
    if day in range(20, 32):
        season = "Spring"
elif month in ("apr", "may"):
    season = "spring"
elif month == "jun":
    if day in range(1, 21):
        season = "spring"
    if day in range(21, 31):
        season = "summer"
elif month in ("jul", "aug"):
    season = "summer"
elif month == "sep":
    if day in range(1, 22):
        season = "summer"
    if day in range(22, 31):
        season = "fall"
elif month in ("oct", "nov"):
    season = "fall"
elif month == "dec":
    if day in range(1, 21):
        season = "fall"
    if day in range(21, 32): 
        season = "winter"
print(f"{month} {day} is in {season}.")
