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
    greeting = (f"Good morning! Today is {date}. The time is {time}. \nIt's breakfast time! Let's find a delicious meal to eat!")
elif hour < 18:
    greeting = (f"Good afternoon! Today is {date}. The time is {time}. \nIt's lunch time! Let's find a delicious meal to eat!")
else:
    greeting = (f"Good evening! Today is {date}. The time is {time}. \nIt's dinner time! Let's find a delicious meal to eat!")

print("{}".format(greeting))

herbivore = "vegetarian"
proteins = "\n\n - Beef\n - Lamb\n - Chicken\n - Seafood\n\n"

#Opening json file
with open('meals.json', 'r') as openfile:
# Reading json file
    json_object = json.load(openfile)["meals"]

# Vegetarian meal and side dish conditional question
diet = input("Do you eat meat? (yes/no): ").lower()
if diet == 'no' and hour < 12:
    print(f"OK here is a mouthwatering {herbivore} breakfast:")
    print(json_object[0]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
elif diet == 'no' and hour < 18:
    print(f"OK here is a mouthwatering {herbivore} lunch:")
    print(json_object[2]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
elif diet == 'no' and hour > 18:
    print(f"OK here is a mouthwatering {herbivore} dinner:")
    print(json_object[12]["mealName"])
    side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
else:
    print("Please enter yes or no")

# Protein meal and side dish conditonal question
protein_option = ''
side_dish = ''
if diet == 'yes':
    protein_option = input(f"OK let's find you a delicious meal.\nChoose from the following protein options: {proteins}").lower()
if protein_option == "beef" and hour < 18:
    print("Here is an exquisite meal suggestion for your lunch:")
    print(json_object[4]["mealName"])
side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == "yes":
    print("Here is a side dish to go with your meal!")
elif protein_option == "beef" and hour > 18:
    print("Here is an exquisite meal suggestion for your dinner:")
    print(json_object[14]["mealName"])

side_dish = input("Would you like a side dish to accompany your meal? (yes/no): ").lower()
if side_dish == "yes":
    print("Here is a side dish to go with your meal!")
    print(json_object[7]["mealName"])





# side_dish  = ''

# if diet == 'no':
#     side_dish = input("Here is an easy yet delicious vegetarian meal:\n\nRECIPE GOES HERE\n\nWould you like a side dish? (yes/no): ").lower()
# elif diet == 'yes':
#     input("Here is an easy yet delicious meal:\n\nRECIPE GOES HERE\n\nWould you like another? (yes/no): ").lower()

# if side_dish == 'yes':
#     print(f"Ok, here is a side dish to your meal:\n\n{}\n\n")
# elif side_dish == 'no':
#     print("Bon Apetit! Buen Provecho! Enjoy your meal!")


