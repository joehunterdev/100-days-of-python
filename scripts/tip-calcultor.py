#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("Whats the bill in dollars?")

people = input("How many people are you?")

percent = input("What the percetage you want to tip?")

per_person = (float(bill) / int(people)) * ( 1 + float(percent)  / 100)
rounded = print("%.2f" % round(per_person, 2))
print(f"{rounded}")
