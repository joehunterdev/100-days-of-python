# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
##365 as int is fine
import math
max_age = 90
remaining_years = max_age - int(age)
weeks_remaining =  (remaining_years * 365) / 12

days = round(remaining_years * 365)
weeks = round(remaining_years * 52)
months = round(remaining_years * 12)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")


/**
#Write your code below this line 👇
##365 as int is fine
import math
max_age = 90
remaining_years = max_age - int(age)
days = remaining_years * 365
weeks = round(days / 7)
months = round(days / 30)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
**/
