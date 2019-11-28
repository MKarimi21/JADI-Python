# Show some tuple ideas in function

X = float(input("Enter your First Number:\n"))
Y = float(input("Enter your Second Number:\n"))

def someMath (X, Y):
    SumXY = X + Y
    MultpleXY = X * Y
    Muple2XY = X ** Y
    RadiXY = X / Y

    return(SumXY, MultpleXY, Muple2XY, RadiXY)

t_somMath = someMath(X, Y)

print("============ Your Result ============","\nYour Sum is: ", t_somMath[0], "\nYour Multiple is: ", t_somMath[1], "\nYour ^2 is: ", t_somMath[2], "\nYour Radical is: ", t_somMath[3])
print("Your result list: ", list(t_somMath))
