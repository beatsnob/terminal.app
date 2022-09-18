from datetime import datetime
from tkinter.tix import INTEGER
# from exceptions import Error

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

class Error(Exception):
    pass

class YesOrNo(Error):
    pass

class NotNumber(Error):
    pass

herbivore = 'vegan or vegetarian'

while True:
    try:
        diet = input("Do you eat meat? (yes/no): ")
        if diet != 'yes''no':
            raise YesOrNo
        elif diet == INTEGER:
            raise NotNumber
        else:
            print("did it")
        break
    except NotNumber:
        print("Please do not enter numbers")
    except YesOrNo:
        print("Please enter yes or no")
    # else:
    #     print(f"OK let's find you a delicious {herbivore} meal")

        # elif diet == int:
        #     raise NotNumber
        # continue
   
    # 
        
   

#     else:print("Please enter yes or no")
#         break



#
# else:
#     print("OK let's find you a delicious meal")

# protein_choice = input(f"Choose from the following protein options: {proteins}")
