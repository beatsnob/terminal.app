from datetime import datetime
from exceptions import Error

today = datetime.today()
now = datetime.now()
hour = now.hour

# Textual month, day and year	
date = today.strftime("%A %B %d, %Y")
time = now.strftime("%H:%M %p")

print(f"Today is, {date}. The time is {time}")

if hour < 12:
    greeting = "Good morning! It's breakfast time! Let's find a delicious meal to eat!"
elif hour < 18:
    greeting = "Good afternoon! It's lunch time! Let's find a delicious meal to eat!"
else:
    greeting = "Good evening! It's time for dinner! Let's find a delicious meal to eat!"

print("{}".format(greeting))

proteins = "\nBeef\nLamb\nChicken\nSeafood"

while True:
    try:
        diet = str(input("Do you eat meat? (yes/no): "))
        if diet != 'yes' 'no':
            raise Exceptions.Error.YesOrNo
        elif diet == int:
            raise Error.NotNumber
        continue
    except Error.YesOrNo:
        print("Please enter yes or no")
        print()
    except Error.NotNumber:
        print("Please do not enter numbers")

#     else:print("Please enter yes or no")
#         break

# herbivore = 'vegan or vegetarian'

# if diet == "yes":
#     print(f"OK let's find you a delicious {herbivore} meal")
# else:
#     print("OK let's find you a delicious meal")

# protein_choice = input(f"Choose from the following protein options: {proteins}")
