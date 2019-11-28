# if, else and elif

r = float(input('Enter Raduse = '))
pi = 3.1415

pizza_areia = (r**2)*pi

if pizza_areia < 150:
    print('Your Pizza is Small and we have')
elif pizza_areia >= 150 and pizza_areia < 300:
    print('Your Pizza is Normal and we have')
elif pizza_areia >= 300 and pizza_areia < 400:
    print('Your Pizza is Big and we have')
else:
    print('We have not your Pizza size')

print('Your Pizza area is =', pizza_areia, 'cm^2')
   
