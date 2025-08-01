for i in range(20):
    if i%4 == 0:
        print(i)
    if i%10 == 0:
        print("Bingo!") 
print("---") 

print(type(10))

# how to use binary octal and hexadecimal
print(0b10)
print(0o10)
print(0x10)
print(type(0o10))
print(.4e7)  # for raised to the power.
print(type(.4e7))

print(1.79e308)
print(type(1.8e308)) 

#complex
a= 6+8j
b = 4 + 9j
print(a+b)
print(type(a))

# String
print(type("I am a string"))

print("This string contains a single quote (') character.")
print('This string contains a single quote (\') character.')

print('a\
... b\
... c') # breaking into multiple lines.

print('foo\tbar')
print("a\141\x61")
print('\u2192 \N{rightwards arrow}')

# #  Activity 1
num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# #  Activity 2
sum = 0
number = int(input("Enter a number and press 0 to terminate: "))
while(True):
    if(number == 0):
        break
    sum += number
    number = int(input("Enter a number and press 0 to terminate: "))

print(f"Sum is {sum}.")

#Activity 3

isPrime = True
primeInput = int(input("Enter a number to check whether it is prime or not: "))
i = 2
while i < primeInput:
    n = primeInput % i
    if n == 0:
        isPrime = False
        break
    else:
        i = i+1
if isPrime:
    print("The number is prime.")
else:
    print("The number is not prime.")

#Activity 4
summation = 0
i = 0
while i<=4:
    inputFiveValues = int(input("Enter a number : "))
    summation += inputFiveValues
    i = i+1

print(f"Sum of 5 input values is : {summation}")

#Activity 5
input = int(input("Enter the value of n: "))
print("Sum : {}".format(input*(input + 1)/2))

s = 0
for i in range(1,101):
    s = s+i

print(s)

print(sum(range(1,101)))

#Activity 6
name = input('What is your name? ') 
print('Hello ' + name)
job = input('What is your job? ') 
print('Your job is ' + job)
num = input('Give me a number? ') 
print('You said: ' + str(num))

# Activity 7

import random

Minimum = 1
Maximum = 9
randomNumber = random.randint(Minimum, Maximum)
Guess = None
Running = True
Try = 0  # Number of attempts

del input
while Running:
    Guess = input("Enter a guess number or type 'exit' to escape: ")

    if Guess.lower() == 'exit':  # Check 'exit' before converting to int
        print("Better luck next time!")
        break

    try:
        Guess = int(Guess)  # Convert input to integer
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Skip this iteration and ask again

    Try += 1  # Increment attempts

    if Guess < randomNumber:
        print("Wrong, too low.")
    elif Guess > randomNumber:
        print("Wrong, too high.")
    else:
        print("Yes, that's the one: {}".format(randomNumber))

        if Try == 1:
            print("Amazing! You guessed it in just 1 try!")
        elif 2 <= Try < 10:
            print("Pretty good, you did it in {} tries.".format(Try))
        else:
            print("Bad tries, you took {} attempts.".format(Try))

        Running = False  # Stop the loop after correct guess

# Lab task -1
import math

userInput = int(input("Enter a number: "))
list = []

while userInput > 1:
    res = math.floor(userInput % 10)
    userInput = userInput/10
    list.append(res)

for i in range(0,len(list)):
    print(list[i],end="")
    i = i+1
print()

# Lab task 2
inputList = []
evenSum = 0
oddSum = 0

while True:
    userInputValue = (input("Enter a value or exit to terminate: "))

    if userInputValue.lower() == 'exit':
        print(f"Even sum is : {evenSum}, Odd sum is : {oddSum}")
        break
    else:
        if int(userInputValue) % 2 == 0:
            evenSum += int(userInputValue)
        else:
            oddSum += int(userInputValue)

# Lab task 3
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(f"Fibonacci of 4 is : {fibonacci(4)}")

fibonacciNumber = int(input("Enter the number to calculate the fibonacci: "))
list = [0,1]
res = 0

if(fibonacciNumber == 0):
    print("Fibonacci is 0")
elif(fibonacciNumber == 1):
    print("Fibonacci is 1")
else:
    fibIndex = 2
    while fibIndex <= fibonacciNumber:
        res = list[fibIndex-1]+list[fibIndex-2]
        fibIndex = fibIndex + 1
        list.append(res)
    print(f"Fibonacci is : {list[fibonacciNumber]}")

# lab task -04

marks = int(input("Enter the marks of the student : "))
if(marks < 50):
    print("Your Grade is F")
elif(marks >= 50 and marks <= 60):
    print("Your Grade is E")
elif(marks >= 61 and marks <= 70):
    print("Your Grade is D")
elif(marks >= 71 and marks <= 80):
    print("Your Grade is C")
elif(marks >= 81 and marks <= 90):
    print("Your Grade is B")
elif(marks >= 91 and marks <= 100):
    print("Your Grade is A")
else:
    print("Please enter marks between 0 and 100.")

# Lab-task 05
userInputForFactorial = int(input("Enter the number to find factorial: "))

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    return num * factorial(num-1)

print(f"Recursive factorial is : {factorial(userInputForFactorial)}")

for i in range(1,userInputForFactorial):
    userInputForFactorial *= i
    i += 1

print(f"Iterative factorial is : {userInputForFactorial}")
