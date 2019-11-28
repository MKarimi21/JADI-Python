# print all prime numbers
# with For in loop

FirstNumber = int(input('Enter First Numbers = '))
LastNumber = int(input('Enter Last Number = '))

for thisNmber in range (FirstNumber, LastNumber):
    isPrime = True
    for counter in range (FirstNumber, thisNmber):
        if ((thisNmber % counter) == 0):
            isPrime = False
    
    if (isPrime):
        print(thisNmber)
