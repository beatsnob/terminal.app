from colorama import init
init()
from datetime import datetime
import json

# Definitions

# # Date and time definitions and display format
today = datetime.today()
now = datetime.now()
hour = now.hour
date = today.strftime("%A %B %d, %Y")
time = now.strftime("%H:%M %p")

#Side dish questions and output
agree = '\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m'
disagree = '\033[35m'"\nNo problems, bon Apetit! Buen Provecho and Enjoy your meal!\n"'\033[39m'
wish = '\033[35m'"Bon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m'

#Greetings
morning = (f"Good morning! Today is {date}. The time is {time}. \nIt's breakfast time! Let's find a delicious meal to eat!\n")
afternoon = (f"Good afternoon! Today is {date}. The time is {time}. \nIt's lunch time! Let's find a delicious meal to eat!\n")
evening = (f"Good evening! Today is {date}. The time is {time}. \nIt's dinner time! Let's find a delicious meal to eat!\n")
side_dish = ''

#Functions
def side_disagree(disagree):
    print(disagree)

def side_agree(agree):
    print(agree)

def bon_apetit(wish):
    print(wish)

def morning_greeting(morning):
    print("{}".format(morning))

def afternoon_greeting(afternoon):
    print("{}".format(afternoon))

def evening_greeting(evening):
    print("{}".format(evening))

#Opening and reading json file
with open('meals.json', 'r') as openfile:
    json_object = json.load(openfile)["meals"]

# Conditional greeting based on the current time
if hour < 12:
    morning_greeting(morning)
    # greeting = (f"Good morning! Today is {date}. The time is {time}. \nIt's breakfast time! Let's find a delicious meal to eat!\n")
elif hour < 18:
    afternoon_greeting(afternoon)
    # greeting = (f"Good afternoon! Today is {date}. The time is {time}. \nIt's lunch time! Let's find a delicious meal to eat!\n")
else:
    evening_greeting(evening)
    # greeting = (f"Good evening! Today is {date}. The time is {time}. \nIt's dinner time! Let's find a delicious meal to eat!\n")

# print("{}".format(greeting))

herbivore = "vegetarian"
proteins = "\n\n - Beef\n - Lamb\n - Chicken\n - Seafood\n\n"
protein_option = ''
side_dish = ''
diet = ''

#Vegetarian question
diet = input('\033[31m'"Do you eat meat? (yes/no): "'\033[39m').lower()

#Vegetarian breakfast
if diet == 'no' and hour < 12:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} breakfast:\n"'\033[39m')
    print(json_object[0]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour < 12:
    side_agree(agree)
    print(json_object[1]["mealName"])
    bon_apetit(wish)
elif side_dish == 'no':
    side_disagree(disagree)

#Vegetarian lunch
elif diet == 'no' and hour < 18:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} lunch:\n"'\033[39m')
    print(json_object[2]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour > 18:
    side_agree(agree)
    print(json_object[3]["mealName"])
    bon_apetit(wish)
# elif side_dish == 'no':
#     side_disagree(disagree)

#Vegetarian dinner
elif diet == 'no' and hour > 18:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} dinner:\n"'\033[39m')
    print(json_object[12]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour > 18:
    side_agree(agree)
    print(json_object[13]["mealName"])
    bon_apetit(wish)
elif side_dish == 'no' and hour > 18:
    side_disagree(disagree)

