#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What was the total bill?\n")
tip_percent = "1." + input("What percentage tip would you like to give?\n")
if len(tip_percent) == 3:
    tip_split = list(tip_percent)
    tip_percent = tip_split[0] + tip_split[1] + "0" + tip_split[2]

people = input("How many people to split the bill?\n")
answer = round((float(bill)/float(people)) * float(tip_percent), 2)
print(f"Each person should pay: ${answer}")