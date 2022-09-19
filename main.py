from datetime import datetime

today = datetime.today()
now = datetime.now()
hour = now.hour

# Date and time display format
date = today.strftime("%A %B %d, %Y")
time = now.strftime("%H:%M %p")

# Conditional greeting based on the current time
if hour < 12:
    greeting = (f"Good morning! Today is {date}. The time is {time}. \nIt's breakfast time! Let's find a delicious meal to eat!")
elif hour < 18:
    greeting = (f"Good afternoon! Today is {date}. The time is {time}. \nIt's lunch time! Let's find a delicious meal to eat!")
else:
    greeting = (f"Good evening! Today is {date}. The time is {time}. \nIt's time for dinner! Let's find a delicious meal to eat!")

print("{}".format(greeting))

# class Error(Exception):
#     pass

# class YesOrNoError(Error):
#     pass

herbivore = "vegan or vegetarian"
proteins = "\n\n - Beef\n - Lamb\n - Chicken\n - Seafood\n\n"
# while True:
#     try:
diet = input("Do you eat meat? (yes/no): ")
if diet == 'no':
    print(f"OK let's find you a delicious {herbivore} meal.")
elif diet == 'yes':
    input(f"OK let's find you a delicious meal.\nChoose from the following protein options: {proteins}")
else:
    print("Please enter yes or no")

second_choice = "SECOND RECIPE GOES HERE"

if diet == 'no':
    another_recipe = input("Here is an easy yet delicious vegetarian meal:\n\nRECIPE GOES HERE\n\nWould you like another? (yes/no): ")
elif diet == 'yes':
    print("Here is an easy yet delicious meal:\n\nRECIPE GOES HERE\n\nWould you like another? (yes/no): ")

if another_recipe == 'yes':
    print(f"Ok, here is another delicious meal:\n\n{second_choice}\n\n")

