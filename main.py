from datetime import datetime
import foods

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

diet = input("Do you eat meat? (yes/no): ")
yes=True
no = False

if diet is True:
    print("OK let's find you a nice meal")
else: diet is False
    # print("thats fine")




# protein_choice = input(f"Choose from the following protein options: {proteins}")
