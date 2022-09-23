from colorama import init
init()
from datetime import datetime
import json
import random

today = datetime.today()
now = datetime.now()
hour = now.hour

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
#Opening json file
with open('meals.json', 'r') as openfile:
# Reading json file
    json_object = json.load(openfile)["meals"]

def random_meal():
    return random.choice(json_object)


# random = random.choice(list(json_object))
random_choice = input("Would you like me to choose a random meal for you? (yes/no): ").lower()

if random_choice == 'yes':
    print('\033[36m'"\nYour randomly selected meal is: "'\033[39m'+ random_meal()["mealName"])

# Vegetarian meal and side dish conditional question    
# while diet not in ('yes', 'no'):
diet = input('\033[31m'"Do you eat meat? (yes/no): "'\033[39m').lower()

#Vegetarian breakfast
if diet == 'no' and hour < 12:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} breakfast:\n"'\033[39m')
    print(json_object[0]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour < 12:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[1]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
    
#Vegetarian lunch
elif diet == 'no' and hour < 18:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} lunch:\n"'\033[39m')
    print(json_object[2]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour < 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[3]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
#Vegetarian dinner
elif diet == 'no' and hour > 18:
    print('\033[33m'f"\nOK here is a mouthwatering {herbivore} dinner:\n"'\033[39m')
    print(json_object[12]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and diet == "no" and hour > 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[13]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
# else:
#         print("Please enter yes or no")


# Protein meal and side dish conditonal question
if diet == 'yes':
    protein_option = input('\033[32m'f"\nOK let's find you a delicious meal.\nChoose from the following protein options: {proteins}"'\033[39m').lower()
#Beef main suggestion and side dish question + conditional
#beef lunch
if protein_option == "beef" and hour < 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your lunch:\n"'\033[39m')
    print(json_object[4]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == "yes" and protein_option == 'beef' and hour < 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[5]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')

#beef dinner
elif protein_option == "beef" and hour > 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your dinner:\n"'\033[39m')
    print(json_object[14]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "beef" and hour > 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[15]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')

#lamb lunch
elif protein_option == "lamb" and hour < 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your lunch:\n"'\033[39m')
    print(json_object[6]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "lamb" and hour < 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!: \nBon Apetit! Buen Provecho! Enjoy your meal!"'\033[39m')
    print(json_object[7]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')

#lamb dinner
elif protein_option == "lamb" and hour > 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your dinner:\n"'\033[39m')
    print(json_object[16]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "lamb" and hour > 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[17]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')

#chicken lunch
elif protein_option == "chicken" and hour < 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your lunch:\n"'\033[39m')
    print(json_object[8]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "chicken" and hour < 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[9]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')

#chicken dinner
elif protein_option == "chicken" and hour > 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your dinner:\n"'\033[39m')
    print(json_object[18]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "chicken" and hour > 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[19]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')

#seafood lunch
elif protein_option == "seafood" and hour < 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your lunch:\n"'\033[39m')
    print(json_object[10]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "seafood" and hour < 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[11]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')

#seafood dinner
elif protein_option == "seafood" and hour > 18:
    print('\033[33m'"\nHere is an exquisite meal suggestion for your dinner:\n"'\033[39m')
    print(json_object[20]["mealName"])
    side_dish = input('\033[31m'"Would you like a side dish to accompany your meal? (yes/no): "'\033[39m').lower()
if side_dish == 'yes' and protein_option == "seafood" and hour > 18:
    print('\033[34m'"\nHere is a side dish to go with your meal!:\n"'\033[39m')
    print(json_object[21]["mealName"])
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')
elif side_dish == 'no':
    print('\033[35m'"\nBon Apetit! Buen Provecho! Enjoy your meal!\n"'\033[39m')