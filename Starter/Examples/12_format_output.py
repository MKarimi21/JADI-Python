# Show output Formatting Scores

scores = [  ['Mostafa Karimi', 18, 17, 16, 18],
            ['Jadi MirMirani', 18, 17, 16, 16],
            ['Sara MirKaimi', 17, 15, 16, 17]
]

for person in scores:
    for item in person:
        if type(item) == str:
            print('{0:18s} |'.format(item), end='')
        else:
            # A =(sum(person[1:4])/4)
            
            print('{0:6.2f} |'.format(item), end='')
    print()
