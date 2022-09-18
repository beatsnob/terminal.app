from datetime import datetime

today = datetime.today()
now = datetime.now()
hour = now.hour

# Textual month, day and year	
date = today.strftime("%A %B %d, %Y")
time = now.strftime("%H:%M %p")

print(f"Today is, {date}. The time is {time}")

if hour < 12:
    greeting = "Good morning! It's breakfast time! What do you feel like eating?"
elif hour < 18:
    greeting = "Good afternoon! It's lunch time! What do you feel like eating?"
else:
    greeting = "Good evening! It's time for dinner! What do you want to eat?" 

print("{}".format(greeting))