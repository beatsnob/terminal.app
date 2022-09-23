from colorama import init
init()
from datetime import datetime
import json
import random


# Definitions

# Date and time definitions and display format
today = datetime.today()
now = datetime.now()
hour = now.hour
date = today.strftime("%A %B %d, %Y")
time = now.strftime("%H:%M %p")

#Side dish questions and outputs
agree = '\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m'
disagree = '\033[35m'"\nNo problems, bon Apetit! Buen Provecho and Enjoy your meal!\n"'\033[39m'
wish = '\033[35m'"Bon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m'
herbivore = "vegetarian"
veg = ('\033[33m'f"\nOK here is a mouthwatering {herbivore} meal:\n"'\033[39m')
meat = ('\033[33m'"\nOK here is a succulent meal:\n"'\033[39m')
proteins = "\n\n - Beef\n - Lamb\n - Chicken\n - Seafood\n\n"
protein_option = ''
side_dish = ''
diet = ''
random_choice = ''

#Greetings
morning = ('\033[33m'f"\nGood morning! Today is {date}. The time is {time}. \nIt's breakfast time! Let's find a delicious meal to eat!\n"'\033[39m')
afternoon = ('\033[33m'f"\nGood afternoon! Today is {date}. The time is {time}. \nIt's lunch time! Let's find a delicious meal to eat!\n"'\033[39m')
evening = ('\033[33m'f"\nGood evening! Today is {date}. The time is {time}. \nIt's dinner time! Let's find a delicious meal to eat!\n"'\033[39m')

#Opening and reading json file
with open('meals.json', 'r') as openfile:
    json_object = json.load(openfile)["meals"]

# #Functions
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

def random_meal():
    return random.choice(json_object)

def order_up_veg(veg):
    print("{}".format(veg))

def order_up_meat(meat):
    print("{}".format(meat))

# Conditional greeting based on the current time
if hour < 12:
    morning_greeting(morning)
elif hour < 18:
    afternoon_greeting(afternoon)
else:
    evening_greeting(evening)

# Random meal selection question and conditionals
while True:
    random_choice = input('\033[31m'"\nWould you like me to choose a random meal for you? (yes/no): "'\033[39m').lower()
    if random_choice == 'yes' or random_choice == 'no':
        break
if random_choice == 'yes':
    print('\033[36m'"\nYour randomly selected meal is: "'\033[39m'+ random_meal()["mealName"])
while True:
    go_on = input('\033[31m'"\nWould you like to continue choosing a meal? (yes/no): "'\033[39m').lower()
    if go_on == 'yes' or go_on == 'no':
        break
if go_on == 'yes':
# Vegetarian meals
    while True:
        diet = input('\033[31m'"\nDo you eat meat? (yes/no): "'\033[39m').lower()
        if diet == 'yes' or diet == 'no':
            break
elif go_on == 'no' and random_choice == 'no':
    print('\033[33m'"\nThank you, see you next time!"'\033[39m')
else:
    bon_apetit(wish)
#Vegetarian breakfast
if random_choice == 'no' and diet == 'no' and hour < 12:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} breakfast:\n"'\033[39m')
    print(json_object[0]["mealName"])
    while True:
        side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
        if side_dish == 'yes' and side_dish == 'no':
            break
if side_dish == 'yes' and diet == "no" and hour < 12:
    side_agree(agree)
    print(json_object[1]["mealName"])
    bon_apetit(wish)
elif side_dish == 'no':
    side_disagree(disagree)
#Vegetarian lunch
elif diet == 'no' and go_on == 'yes' and hour < 18:
    order_up_veg(veg)
    print(json_object[2]["mealName"])
    while True:
        side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
        if side_dish == 'yes' and side_dish == 'no':
            break
if side_dish == 'yes' and diet == "no" and hour < 18:
    side_agree(agree)
    print(json_object[3]["mealName"])
    bon_apetit(wish)
elif side_dish == 'no' and hour < 18:
    side_disagree(disagree)
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

# Protein meals
if diet == 'yes':
    while True:
        protein_option = input('\033[32m'f"\nOK let's find you a delicious meal.\nChoose from the following protein options: {proteins}"'\033[39m').lower()
        if protein_option == 'beef' or protein_option == 'lamb' or protein_option == 'chicken' or protein_option == 'seafood':
            break
# Beef lunch
if protein_option == "beef" and hour < 18:
    order_up_meat(meat)
    print(json_object[4]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == "yes" and protein_option == 'beef' and hour < 18:
    side_agree(agree)
    print(json_object[5]["mealName"])
    bon_apetit(wish)
#beef dinner
elif protein_option == "beef" and hour > 18:
    order_up_meat(meat)
    print(json_object[14]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "beef" and hour > 18:
    side_agree(agree)
    print(json_object[15]["mealName"])
    bon_apetit(wish)
#lamb lunch
elif protein_option == "lamb" and hour < 18:
    order_up_meat(meat)
    print(json_object[6]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "lamb" and hour < 18:
    side_agree(agree)
    print(json_object[7]["mealName"])
    bon_apetit(wish)
#lamb dinner
elif protein_option == "lamb" and hour > 18:
    order_up_meat(meat)
    print(json_object[16]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "lamb" and hour > 18:
    side_agree(agree)
    print(json_object[17]["mealName"])
    bon_apetit(wish)
#chicken lunch
elif protein_option == "chicken" and hour < 18:
    order_up_meat(meat)
    print(json_object[8]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "chicken" and hour < 18:
    side_agree(agree)
    print(json_object[9]["mealName"])
    bon_apetit(wish)
#chicken dinner
elif protein_option == "chicken" and hour > 18:
    order_up_meat(meat)
    print(json_object[18]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "chicken" and hour > 18:
    side_agree(agree)
    print(json_object[19]["mealName"])
    bon_apetit(wish)
#seafood lunch
elif protein_option == "seafood" and hour < 18:
    order_up_meat(meat)
    print(json_object[10]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "seafood" and hour < 18:
    side_agree(agree)
    print(json_object[11]["mealName"])
    bon_apetit(wish)
#seafood dinner
elif protein_option == "seafood" and hour > 18:
    order_up_meat(meat)
    print(json_object[20]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "seafood" and hour > 18:
    side_agree(agree)
    print(json_object[21]["mealName"])
    bon_apetit(wish)
elif side_dish == 'no':
    side_disagree(disagree)