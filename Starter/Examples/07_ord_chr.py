# Ord and chr with escape sequencing
# escape sequencing: search in Web

A = int(input('Enter first number = '))
B = int(input('Enter Last Number = '))
C = " "
for character in range(A,B):
    C = C + chr(character)

print('Your Result of Chaarter in UTF-8\nmaybe in AC is : ') 
print(C)
