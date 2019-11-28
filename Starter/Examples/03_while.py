# a program to calculate the square root with While
# Babylian Algorithm for Square

Number = float(input('Give me N, I whill give you the Square(N) : '))
error = 0.001
guess = abs(Number / 2)
iteraion = 0
if Number <= 0:
    Number = abs(Number)
    print('Your Number is incorrect and agian run program whith abslute number')
    
else:
    while (abs(Number-guess**2) > error):
        iteraion = iteraion + 1
        print('-> on iteration', iteraion, 'my guess is', guess)
        tqs = Number / guess
        guess = (tqs + guess) / 2

print ('The square root is', Number, ' is', guess)
