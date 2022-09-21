from colorama import init
init()
from datetime import datetime
import json

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

#Opening json file
with open('meals.json', 'r') as openfile:
# Reading json file
    json_object = json.load(openfile)["meals"]

# Vegetarian meal and side dish conditional question

diet = input("Do you eat meat? (yes/no): ").lower()
#Vegetarian breakfast
if diet == 'no' and hour < 12:
    print(f"\nOK here is a mouthwatering {herbivore} breakfast:\n")
    print(json_object[0]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and diet == "no" and hour < 12:
    print("\nHere is a side dish to go with your meal!:\n")
    print(json_object[1]["mealName"])
#Vegetarian lunch
elif diet == 'no' and hour < 18:
    print(f"\nOK here is a mouthwatering {herbivore} lunch:\n")
    print(json_object[2]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and diet == "no" and hour < 18:
    print("\nHere is a side dish to go with your meal!:\n")
    print(json_object[3]["mealName"])
#Vegetarian dinner
elif diet == 'no' and hour > 18:
    print(f"\nOK here is a mouthwatering {herbivore} dinner:\n")
    print(json_object[12]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and diet == "no" and hour > 18:
    print("\nHere is a side dish to go with your meal!:\n")
    print(json_object[13]["mealName"])
elif side_dish == 'no':
    print("\nBon Apetit! Buen Provecho! Enjoy your meal!\n")
# else:
#     print("Please enter yes or no")

# Protein meal and side dish conditonal question
if diet == 'yes':
    protein_option = input(f"\nOK let's find you a delicious meal.\nChoose from the following protein options: {proteins}").lower()
#Beef main suggestion and side dish question + conditional
#beef lunch
if protein_option == "beef" and hour < 18:
    print("\nHere is an exquisite meal suggestion for your lunch:\n")
    print(json_object[4]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == "yes" and protein_option == 'beef' and hour < 18:
    print("\nHere is a side dish to go with your meal!\n")
    print(json_object[5]["mealName"])
#beef dinner
elif protein_option == "beef" and hour > 18:
    print("\nHere is an exquisite meal suggestion for your dinner:\n")
    print(json_object[14]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and protein_option == "beef" and hour > 18:
    print("\nHere is a side dish to go with your meal:\n")
    print(json_object[15]["mealName"])

#lamb lunch
elif protein_option == "lamb" and hour < 18:
    print("\nHere is an exquisite meal suggestion for your lunch:\n")
    print(json_object[6]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and protein_option == "lamb" and hour < 18:
    print("\nHere is a side dish to go with your meal:\n")
    print(json_object[7]["mealName"])
#lamb dinner
elif protein_option == "lamb" and hour > 18:
    print("\nHere is an exquisite meal suggestion for your dinner:\n")
    print(json_object[16]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and protein_option == "lamb" and hour > 18:
    print("\nHere is a side dish to go with your meal:\n")
    print(json_object[17]["mealName"])

#chicken lunch
elif protein_option == "chicken" and hour < 18:
    print("\nHere is an exquisite meal suggestion for your lunch:\n")
    print(json_object[8]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and protein_option == "chicken" and hour < 18:
    print("\nHere is a side dish to go with your meal:\n")
    print(json_object[9]["mealName"])
#chicken dinner
elif protein_option == "chicken" and hour > 18:
    print("\nHere is an exquisite meal suggestion for your dinner:\n")
    print(json_object[18]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and protein_option == "chicken" and hour > 18:
    print("\nHere is a side dish to go with your meal:\n")
    print(json_object[19]["mealName"])

#seafood lunch
elif protein_option == "seafood" and hour < 18:
    print("\nHere is an exquisite meal suggestion for your lunch:\n")
    print(json_object[10]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and protein_option == "seafood" and hour < 18:
    print("\nHere is a side dish to go with your meal:\n")
    print(json_object[11]["mealName"])
#seafood dinner
elif protein_option == "seafood" and hour > 18:
    print("\nHere is an exquisite meal suggestion for your dinner:\n")
    print(json_object[20]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == 'yes' and protein_option == "seafood" and hour > 18:
    print("\nHere is a side dish to go with your meal:\n")
    print(json_object[21]["mealName"])

# else:
#     print("Please enter yes or no")

# #Side dish conditionals
# side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
# if side_dish == "yes" and protein_option == 'beef' and hour < 18:
#     print("Here is a side dish to go with your meal!")
#     print(json_object[5]["mealName"])
# elif side_dish == 'yes' and protein_option == "beef" and hour > 18:
#     print("Here is an exquisite meal suggestion for your dinner:")
#     print(json_object[15]["mealName"])
# else:
#     print("Please enter yes or no")

# side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
# if side_dish == "yes":
#     print("Here is a side dish to go with your meal!")
#     print(json_object[7]["mealName"])





# side_dish  = ''

# if diet == 'no':
#     side_dish = input("Here is an easy yet delicious vegetarian meal:\n\nRECIPE GOES HERE\n\nWould you like a side dish? (yes/no): ").lower()
# elif diet == 'yes':
#     input("Here is an easy yet delicious meal:\n\nRECIPE GOES HERE\n\nWould you like another? (yes/no): ").lower()

# if side_dish == 'yes':
#     print(f"Ok, here is a side dish to your meal:\n\n{}\n\n")



