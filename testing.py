from colorama import init
init()
from datetime import datetime
import json

# Definitions
today = datetime.today()
now = datetime.now()
hour = now.hour
agree = '\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m'
disagree = 'buen provecho'
side_dish = ''

#Functions

def side_disagree(disagree):
    print(disagree)

def side_agree(agree):
    print(agree)

#Opening and reading json file
with open('meals.json', 'r') as openfile:
    json_object = json.load(openfile)["meals"]

# Date and time display format
date = today.strftime("%A %B %d, %Y")
time = now.strftime("%H:%M %p")

# Conditional greeting based on the current time
if hour < 12:
    greeting = (f"Good morning! Today is {date}. The time is {time}. \nIt's breakfast time! Let's find a delicious meal to eat!\n")
elif hour < 18:
    greeting = (f"Good afternoon! Today is {date}. The time is {time}. \nIt's lunch time! Let's find a delicious meal to eat!\n")
else:
    greeting = (f"Good evening! Today is {date}. The time is {time}. \nIt's dinner time! Let's find a delicious meal to eat!\n")

print("{}".format(greeting))

herbivore = "vegetarian"
proteins = "\n\n - Beef\n - Lamb\n - Chicken\n - Seafood\n\n"
protein_option = ''
side_dish = ''
diet = ''

# Vegetarian meal and side dish conditional question
# while diet not in ('yes', 'no'):
diet = input('\033[31m'"Do you eat meat? (yes/no): "'\033[39m').lower()
#Vegetarian breakfast
if diet == 'no' and hour < 12:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} breakfast:\n"'\033[39m')
    print(json_object[0]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour < 12:
    side_agree(agree)
    print(json_object[1]["mealName"])
elif side_dish == 'no':
    side_disagree(disagree)
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
    #Vegetarian lunch
elif diet == 'no' and hour < 18:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} lunch:\n"'\033[39m')
    print(json_object[2]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour < 18:
    side_agree(agree)
    print(json_object[3]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
elif side_dish == 'no':
    side_disagree(disagree)
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
#Vegetarian dinner
elif diet == 'no' and hour < 23:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} dinner:\n"'\033[39m')
    print(json_object[12]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour < 23:
    side_agree(agree)
    print(json_object[13]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
elif side_dish == 'no':
    side_disagree(disagree)
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')


# side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
# if side_dish == 'yes' and diet == 'no':
#     side_agree(agree)
#     print(json_object[1]["mealName"])
# elif side_dish == 'no':
#     side_disagree(disagree)