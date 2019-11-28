# print all prime numbers
# have bug becuse print firstNumber to lastNumber +1 not print prime number

FirstNumber = int(input('Enter First Numbers = '))
LastNumber = int(input('Enter Last Number = '))

while FirstNumber < LastNumber + 1:
    isPrimeNumber = True
    counter = FirstNumber
    while counter < FirstNumber - 1:
         if ((FirstNumber % counter) == 0):
             isPrimeNumber = False
             break
         counter += 1
    
    if isPrimeNumber:
        print(counter)
    FirstNumber += 1
