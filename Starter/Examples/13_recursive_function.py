# recursive function for factorial and some

N = int(input("Enter your Number: "))

def factorial(N):
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)
def adder(N):
    if N <= 1:
        return 1
    else:
        return N + adder(N-1)

print('Your', N, 'factorial is: ', factorial(N), '\nand your sum', N, 'is: ', adder(N))
