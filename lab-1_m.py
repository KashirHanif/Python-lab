print("hey there")

x=2
if x==2:
    print("x is 2")

type(x)
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

for i in range(5):
    print(i)

print("now while loop")
counter = 0
while counter < 5:
    print(counter)
    counter += 1

x = 5
y = "John"
print(type(x))
print(type(y))

x = 5    
y = 3.2  

z = x + y  
print(z)   

x = 5
y = float(x)  
print(y)      

x = 7.9
y = int(x)    
print(y)      

x = 10
y = str(x)    
print(y)      

x = "20"
y = int(x)    
print(y)      

print("{} is odd and so is {} and {}".format(3,5,7))
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "MALEAHA"
print(a[1])
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
 
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello,
World!'''
word = "Python"
print(word[1:4])
print(word[:4])
print(word[2:])

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

b = "Hello, World!"
print(b[-5:-2])

my_list = [1, 2, 3, 4, 5]
print(my_list)

mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)

nested_list = [1, [2, 3], 4]
print(nested_list)

my_list = [10, 20, 30]
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
my_list.extend([50, 60])
print(my_list)

my_set = {1, 2, 3, 4}
print(my_set)
my_set.add(5)
print(my_set)
my_set.remove(3)
print(my_set)
my_set.add(5)
print(my_set)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

class Dog:
    def _init_(self, name, age):
        self.name = name
        self.age = age
   
    def bark(self):
        print(f"{self.name} says woof!")
   
    def describe(self):
        print(f"{self.name} is {self.age} years old.")

my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()
my_dog.describe()

class Dog:
    def _init_(self, name, age):
        self.name = name
        self.age = age
   
    def bark(self):
        print(f"{self.name} says woof!")
   
    def describe(self):
        print(f"{self.name} is {self.age} years old.")
   
    def dog_years(self):
        dog_years = self.age * 7
        print(f"{self.name} is {dog_years} dog years old.")

my_dog = Dog("Buddy", 3)
my_dog.dog_years()

class Animal:
    def _init_(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def _init_(self, name):
        super()._init_("Cat")
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} says meow!")

tom = Cat("Tom")
tom.make_sound()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

from datetime import datetime
now = datetime.now()
print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))