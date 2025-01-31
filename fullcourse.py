#http://pypi.org
#https://www.youtube.com/watch?v=_uQrJ0TkZlc
import math
from pathlib import Path
import converter
from converter import kg_to_lbs
from utils import find_max
import ecommerce.shipping
import random
import requests


print(math.ceil(2.9))#3
print(math.floor(2.9))#2
print(" ")

#exercise 0
#python 3 math module 
#name = input('What is your name? ')
#print('Hi ' + name)
#birth = input('Birth year: ')
#print(type(birth))#<class 'str'>
#age = 2022 - int(birth)
#print(type(age))#<class 'int'>
#print(age)

"""print('''Hi John,
This is our first email to you
Thank you,
The support team''')
print(" ")
print('*' * 10)#**********
"""
course = 'Python for Beginners'
print(course[-2])#r
print(course[0:3])#Pyt
"""
print(course[1:])#ython for Beginners
print(course[:5])#Pytho
print(course[1:-1])#ython for Beginner
print(len(course))#20 (including spaces)
print(course.upper())#PYTHON FOR BEGINNER
print(course.lower())#python for beginner
print(course.find('Beginners'))#11 (starts at index 11)
print(course.find('0'))#-1
print(course.replace('Beginners', 'Absolute Beginners'))#Python for Absolute Beginners
print('Python' in course)#True
print('python' in course)#False (case sensitive)
another = course[:]#copy course
print(another)#Python for Beginners
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)#John [Smith] is a coder
print(msg)#John [Smith] is a coder
print(10/3)#3.3333333333333335
print(10//3)#3
print(10**3)#1000
x=2.9
print(round(x))#3
print(" ")
"""

#exercise 1
is_hot=False
is_cold=True
if is_hot:#if it's warm
  print("It's a hot day")
  print("Drink plenty of water")
elif is_cold:#if it's cold
  print("It's a cold day")
  print("Wear warm clothes")
else:#if it's neither
  print("It's a lovely day")
print("Enjoy yout day!")#out of if
print(" ")

#exercise 2
price = 1000000
has_good_credit = True
if has_good_credit:
  down_payment = 0.1 * price
else:
  down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
print(" ")

#exercise 3
has_high_income = True #False doesn't show anything
has_criminal_record = False
if has_high_income and has_good_credit:
  print("Eligible for loan")
print(" ")

#exercise 3
if has_good_credit and not has_criminal_record:
  print("Eligible for loan")
print(" ")

#exercise 5
temperature = 35
if temperature >= 30:
  print("It's a hot day")
else:
  print("It's not a hot day")
print(" ")

#exercise 6
"""
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
  converted = weight * 0.45
  print(f"You are {converted} kilos")
else:
  converted = weight/0.45
  print(f"You are {converted} pounds")
"""
i=1
while i<=5:
  print(i)
  i = i + 1
print("Done")#1 2 3 4 5
print(" ")

j=1
while j<=5:
  print('*' * j)
  j = j + 1
print("Done")
print(" ")

#exercise 7
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input('Guess: '))
  guess_count += 1
  if guess == secret_number:
    print('You won!')
    break
  else:
    print('Sorry, you failed')
    
#exercise 8
"""command = ""
started = False
while True:
  command = input("> ").lower()
  if command == "start":
    if started:
      print("Car is already started!")
    else:
      started = True
      print("Car started...")
  elif command == "stop":
    if not started:
      print("Car is already stopped")
    else:
      started = False
      print("Car stopped")
  elif command == "help":
    print('''
    start - to start the car
    stop - to stop the car
    quit - to quit
    ''')
  elif command == "quit":
    break
  else:
    print("Sorry, I don't understand that")
"""

for item in 'Python':
  print(item)#prints every letter in python
print(" ")
for item in range(10):
  print(item)#prints 0,1,2,3,4,5,6,7,8,9
print(" ")
for item in [1, 2, 3, 4, 5, 6, 7]:
  print(item)#prints 1,2,3,4,5,6,7
print(" ")
for item in range(5, 10):
  print(item)#prints 5,6,7,8,9
print(" ")
for item in range(5, 10, 2):
  print(item)#prints 5,7,9
print(" ")

"""
#exercise 9
prices = [10, 20, 30]
total = 0
for item in prices:
  total += item
print(f"Total: {total}")
print(" ")

#exercise 10
for x in range(4):
  for y in range(3):
    print(f'({x}, {y})')
print(" ")

#exercise 11
numbers = [5, 2, 5, 2, 2]
for x in numbers:
  #print('x' * x)
  output = ''
  for count in range(x):
    output += 'x'
  print(output)
print(" ")

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])#John
print(names[-1])#Mary
print(names[2:])#['Mosh', 'Sarah', 'Mary']
print(names[2:4])#['Mosh', 'Sarah']
print(names[2:5])#['Mosh', 'Sarah', 'Mary']
print(" ")
names[0] = 'Jon'
print(names)
print(" ")

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
  if number > max:
    max = number
print(max)
print(" ")
numbers.append(20)#20 is added at the end of this list
numbers.append(6)#6 is added at the end of this list
numbers.insert(0, 10)#10 is added at the beginning of the list
#numbers.remove(6)#6 is removed
#numbers.clear()#it empties our list
#numbers.pop()#the last number is removed
print(numbers.index(6))#2
print(numbers.count(6))#2
print(50 in numbers)#False
#print(numbers.sort())#none
uniques = []
for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)
numbers2 = numbers.copy()
print(numbers2)
numbers.sort()
numbers.reverse()#descending order
print(numbers)
print(" ")

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]  
]
#matrix[0][1] = 20
print(f"(0,1) matrix: {matrix[0][1]}")
print(" ")

for row in matrix:
  for item in row:
    print(item)
print(" ")

numbers3 = (1, 2, 3)
print(numbers3[0])
print(" ")

#tuples can't be modified
coordinates = (1, 2, 3) 
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]
x, y, z = coordinates
print(y)#2
print(" ")"""

customer = {
  "name": "John Smith",
  "age": 30,
  "is_verified": True
}
#print(customer["name"])
#print(customer["birthday"])#error
print(customer.get("name"))
print(customer.get("birthday"))#none
print(customer.get("birthday", "Jan 1 1980"))#Jan 1 1980
print(" ")

#exercise 12
"""
phone = input("Phone: ")
digits = {
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four"
}
output = ""
for ch in phone:
  output += digits.get(ch, "!") + " "
print(output)
print(" ")

message = input(">")
words = message.split(' ')
print(words)#['Good', 'morning']
emojis = { 
  ":)": "(smiley face)",
  ":(": "(sad face)"
}
output = ""
for word in words:
 output += emojis.get(word, word) + " "
print(output)
"""

def greet(first_name, last_name): 
  print(f'Hi {first_name} {last_name}!')
  print('Welcome aboard')


print("Start")
greet(last_name = "Smith", first_name = "John")
print("Finish")
print(" ")

def square(number):
  return number*number
print(square(3))
print(" ")


"""
def emoji(message):
  words = message.split(' ')
  #print(words)#['Good', 'morning']
  emojis = { 
    ":)": "(smiley face)",
    ":(": "(sad face)"
  }
  output = ""
  for word in words:
   output += emojis.get(word, word) + " "
  return output

message = input(">")
print(emoji(message))
"""

"""
#exception
try:
  age = int(input('Age: '))
  income = 20000
  risk = income/age
  print(age)
except ZeroDivisionError:
  print('Age cannot be 0')
except ValueError:
  print('Invalid value')
print(" ")
"""

#classes
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def move(self):
    print("move")
    
  def draw(self):
    print("draw")
"""
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x) 
"""

point = Point(10,20)
point.x = 11
print(point.x)
print(" ")

class Person:
  def __init__(self, name):
    self.name = name
  def talk(self):
    print(f"Hi, I am {self.name}")

john = Person("John Smith")
#print(john.name)
john.talk()

bob = Person("Bob Smith")
bob.talk()
print(" ")

#inheritance
class Mammal:
  def walk(self):
    print("walk")
  
class Dog(Mammal):
  def bark(self):
    print("bark")


class Cat(Mammal):
  def be_annoying(self):
    print("annoying")
cat1 = Cat()
cat1.be_annoying()
dog1 = Dog()
dog1.walk()
print(" ")

#Module
#converter

#Ctrl + Space

print(kg_to_lbs(100))#222.22222222222223
print(converter.kg_to_lbs(70))#155.55555555555554
print(" ")

#utils

numbers = [10, 3, 6, 2]
max = find_max(numbers)
print(max)
#print(max(numbers))
print(" ")


ecommerce.shipping.calc_shiping()
print(" ")

#Random module

for i in range(3):
  print(random.random())
  print(random.randint(10,20))#for int
members = ['John', 'Mary', 'Bob', 'Mosh']
print(random.choice(members))
print(" ")

class Dice:
  def roll(self):
    first = random.randint(1,6)
    second = random.randint(1,6)
    return (first, second)

dice = Dice()
print(dice.roll())
print(" ")

#Pathlib module

#Absolute path
#c:\program Files\Microsoft
#/usr/local/bin
#Relative Path
path2 = Path("ecommerce")
path1 = Path("ecommerce1")
path = Path()
path0 = Path("email")
print(path2.exists())#True
print(path1.exists())#False
print(path.glob('*.py'))#<generator object Path.glob at 0x7f878ff16eb0>
print(" ")
#we use glob to search for files
#* all the files and directories in the current path
#*.* all the files
#*.py all the .py files 
#print(path0.mkdir())#None (create email directory)
#print(path0.rmdir())#Remove directory
for file in path.glob('*.py'):
  print(file)
print(" ")
for file in path.glob('*'):
  print(file)

#Exercise 13
#On terminal: pip install requests

# Your Yelp API Key
API_KEY = 'INSERT_YOUR_API_KEY_HERE'

# API endpoint for search
url = 'https://api.yelp.com/v3/businesses/search'

# Search parameters
params = {
    'term': 'barber',          # Search for barber shops
    'location': 'New York',    # Location
    'sort_by': 'rating',       # Sort by rating
    'limit': 5                 # Maximum number of results
}

# Headers for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}'
}

# Send the request to the API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract JSON data
    data = response.json()
    
    # Display the results
    for business in data['businesses']:
        print(f"Name: {business['name']}")
        print(f"Rating: {business['rating']}")
        print(f"Address: {', '.join(business['location']['display_address'])}")
        print(f"Phone: {business['phone']}")
        print(f"Link: {business['url']}")
        print('-' * 40)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
