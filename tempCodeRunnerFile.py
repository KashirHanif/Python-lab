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