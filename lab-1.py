
print("Hello World")

if(5 > 2):
    print("Five is greater than 2")
    
#this is how we write single line comment in python.

"""
this is how we write 
multiline comment
"""

print("""This is kashir 
      how are you?""")

x = 5
y = 10;
if(x < y):
    print("{} is less than {}".format(x,y))
else:
     print("{} is greater than {}".format(x,y))

# variable name cannot start from digit like 2myvar is not allowed
# variable name cannot contain - like my-var is not allowed
# variable name cannot contain space like my var is not allowed

# all other ways of writing variables names is allowed

#Camel Case:
myName = "Kashir"
print(myName);

#Pascal case:
MyName = "Kashir"

# Snake case:
my_name = "Kashir"

# we can also declare multiple variables at the same line:
per1, per2, per3 = "kashir","hamza","ali"
print(per1,per2,per3);

# we can also unpack a list like that:
names = ["kashir","hamza","ahmed"]
x,y,z = names
print(x,y,z)

for i in range(1,11):
    print("5 multiply ",i, " is : ", 5*i)
    
choice = "head"
type(choice)

i=0
while i < 5:
    print(i)
    i=i+1


if(0):
    print("0 is false")
elif("str"):
    print("String is true");
else:
    print("Nothing is true");

choices = any([True,False]) # it will be true because any of the two has to be true
print(choices)

choices = all([True,False]) # it will be false because both of the two has to be true
print(choices)

# Number data type is of three types: int, float and complex where complex has real and imaginary part
num1 = 5+3j
num2 = complex(2,5);

print(num1.real,num1.imag);

print(abs(-5.5))
print(round(5.99,1)) # the second parameter gives the decimal places. so it;s answer will be 6.0

# tuples are immutable

t = (1,2,3,4,5)
print("Tuple is : ")
for i in t:
    print(i)
    
fruits = ["apple","banana","orange"]
print(fruits[1])
type(fruits)
#print("After type casting of list into tuple: ")
#fruits = tuple(fruits)

set = {3,2,1,4,5}
type(set)

for i in set:
    print(i)
 
dictionary = {"car":"audi", "price": 2400000,"color":"red"}
x = dictionary.keys();
print(x)

dictionary = {"car":"audi", "price": 2400000,"color":"red"}
y = dictionary.values();
print(y)

dictionary["car"]

dictionary["model"] = "2005"
print(dictionary)

del dictionary["price"]
print(dictionary)

dictCopy = dictionary.copy()
print(dictCopy)

# the only way to create constants in python is through Enum
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

age = input("Enter your age? : ")
print(f"Your age is : {age}")

print(State.ACTIVE.value) # we cannot reassign the value like State.ACTIVE.value = 2 -> it is not allowed.
print(len(State))
    
class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self, item):
        # Add an item to the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the top item from the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        # Return the top item without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def size(self):
        # Return the number of items in the stack
        return len(self.stack)

    def display(self):
        # Display the stack
        if not self.is_empty():
            return self.stack
        else:
            return "Stack is empty!"
        
s1 = Stack()
s1.push(10)
s1.display()
[10]
 