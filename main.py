from datetime import datetime
import foods
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

# second_choice = "SECOND RECIPE GOES HERE" - replaced with side dish instead
# Instances of meal class from foods
# Vegetarian meals
breakfast_main_veg = foods.Meal('Vegetarian', 'Breakfast', 'Main meal')
breakfast_side_veg = foods.Meal('Vegetarian', 'Breakfast', 'Side dish')
lunch_main_veg = foods.Meal('Vegetarian', 'Lunch', 'Main meal')
lunch_side_veg = foods.Meal('Vegetarian', 'Lunch', 'Side dish')
dinner_main_veg = foods.Meal('Vegetarian', 'Dinner', 'Main meal')
dinner_side_veg = foods.Meal('Vegetarian', 'Dinner', 'Side dish')
# Meat based meals
breakfast_main_meat = foods.Meal('Meat', 'Breakfast', 'Main meal')
breakfast_side_meat = foods.Meal('Meat', 'Breakfast', 'Side dish')
lunch_main_beef = foods.Meal('Beef', 'Lunch', 'Main meal')
lunch_side_beef = foods.Meal('Beef', 'Lunch', 'Side dish')
dinner_main_beef = foods.Meal('Beef', 'Dinner', 'Main meal')
dinner_side_beef = foods.Meal('Beef', 'Dinner', 'Side dish')
lunch_main_lamb = foods.Meal('Lamb', 'Lunch', 'Main meal')
lunch_side_lamb = foods.Meal('Lamb', 'Lunch', 'Side dish')
dinner_main_lamb = foods.Meal('Lamb', 'Dinner', 'Main meal')
dinner_side_lamb = foods.Meal('Lamb', 'Dinner', 'Side dish')
lunch_main_chicken = foods.Meal('Chicken', 'Lunch', 'Main meal')
lunch_side_chicken = foods.Meal('Chicken', 'Lunch', 'Side dish')
dinner_main_chicken = foods.Meal('Chicken', 'Dinner', 'Main meal')
dinner_side_chicken = foods.Meal('Chicken', 'Dinner', 'Side dish')
lunch_main_seafood = foods.Meal('Seafood', 'Lunch', 'Main meal')
lunch_side_seafood = foods.Meal('Seafood', 'Lunch', 'Side dish')
dinner_main_seafood = foods.Meal('Seafood', 'Dinner', 'Main meal')
dinner_side_seafood = foods.Meal('Seafood', 'Dinner', 'Side dish')


side_dish  = ''
if diet == 'no':
    side_dish = input("Here is an easy yet delicious vegetarian meal:\n\nRECIPE GOES HERE\n\nWould you like a side dish? (yes/no): ")
elif diet == 'yes':
    print("Here is an easy yet delicious meal:\n\nRECIPE GOES HERE\n\nWould you like another? (yes/no): ")

if side_dish == 'yes':
    print(f"Ok, here is a side dish to your meal:\n\n{lunch_side_beef}\n\n") #unsure about how to incorporate the attributes of the instances
elif side_dish == 'no':
    print("Bon Apetit! Buen Provecho! Enjoy your meal!")

# Opening JSON file
with open('meals.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)["meals"]
 
print(json_object[0]["mealName"])
