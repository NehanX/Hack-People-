from time import sleep
from random import choice, randint
import calendar, datetime

# Copyright (c) 2021 Nehan Nizami & Azhaan Salam

emails = [
    "theidiot@dogwater.net", "theidiot@dogwater.com",
    "whydoes@everyonehate.me", "morelike@absolute.garbage", "-rando@noob.net",
    "thenoob@im.trash", "akaMRdumbo@im.stupid"
]
lastNames = [
    "the Idiot", "the Actual Captain Underpants", "the Bug", "the Rando",
    "the Teammate Everyone Hates"
]
randomMessage = [
    "Bob", "Ryan", "noob", "George", "oh wait no", "dont no u", "bruh",
    "hahahhahahahahahahahahaha"
]
latestMessage = [
    f"no u {choice(randomMessage)}", "I am dumb", "I am stupid",
    f"hello {choice(randomMessage)}", f"{choice(randomMessage)} stupid",
    "STOP", "STOP I WILL BLOCK U", "STOP I WILL BLOC U",
    "follow azh412 on GitHub",
    "This isnt a rickroll --> https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "drama hahahhahahahahahahahahaha", "e", "I been watching peppa pig",
    "u a boomer", "ok", "ok boomer"
]

print("Hello, welcome to Hack People.")
answer = input(" Who would you like to hack? ")
sleep(randint(1, 3))
print(f'Hacking user {answer}...')
sleep(randint(1, 3))
print('obtaining personal info')
sleep(randint(1, 3))
strforemails = "-".join(answer.split())
print(f'Email: {strforemails}{choice(emails)}')
sleep(randint(1, 3))
print(f'Password: {answer} {choice(lastNames)}')
sleep(randint(1, 3))
print('Obtaining Earnings Amount...')
sleep(randint(1, 3))
money = -randint(0, 200)
moneyToRupees = money * 73
print(f'General Earnings: {money}')
print('Salary: 0')
print(f'Rupees: {moneyToRupees}')
sleep(randint(1, 3))
print('Hacking Credit Card')
sleep(randint(1, 3))
print(
    f'Credit Card: {randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)}'
)
sleep(randint(1, 3))
print(f'CVC Code: {randint(100, 999)}')
sleep(randint(1, 3))
print(f'Full Name: {answer} {choice(lastNames)}')
sleep(randint(1, 3))
year = randint(1950, 2032)
cal = calendar.TextCalendar()
aaa = randint(1, 12)
datetime_object = datetime.datetime.strptime(str(aaa), "%m")
month_name = datetime_object.strftime("%B")
print(f'Expiration Date: {month_name} {year}')
sleep(randint(1, 3))
if year < 2021:
	print("this idiot better not buy anything with that piece of expired garbage")
if aaa < 5 and year == 2021:
	print("this idiot better not buy anything with that piece of expired garbage")
sleep(randint(1, 3))

print("Obtaining Latest Messages")
sleep(randint(1, 3))
print(f'"{choice(latestMessage)}"')

print('Obtaining IP')
sleep(randint(1, 3))
print(
    f'IP: {randint(10, 999)}.{randint(10, 999)}.{randint(10, 999)}.{randint(10, 999)}'
)
sleep(randint(1, 3))
print('Now that its been enough..')
sleep(randint(1, 3))
print('You are the one being hacked')
sleep(randint(1, 3))
print('Personal Info Obtained.')
sleep(randint(1, 3))
print('Credit Cards Obtained')
sleep(randint(1, 3))
print('IP Address Obtained')
sleep(randint(1, 3))
response = input('You seriously believed that? ')

if response == 'yes':
	print("Wow, how dogwater of you")
elif response == 'no':
	print("Wow, you're dogwater for lying")
else:
	print("You were supposed to say yes or no -_-")
	sleep(1)
	print("Use ur common sense")

print('Goodbye punk')
