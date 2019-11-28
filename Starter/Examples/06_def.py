# a program to calculate the square root with def
# Babylian Algorithm for Square

def Square(Number):
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
    

Number = float(input('Give me N, I whill give you the Square(N) : '))
print('Your Number is = ', Number)
Square(Number)
Num2 = Number**2
print('Your Number ^2 is = ', Num2 )
Square(Number**2)
