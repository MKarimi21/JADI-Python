# calculate person score in list 

scores = [
            ['Mostafa', 15, 18, 19, 17],
            ['JADI', 17, 16, 20, 19],
            ['MIR', 13, 12, 16, 17]
    ]

for person in scores:
    total = 0
    for i in range(1, len(person)):
        total = total + person[i]
    average = total / (len(person) -1)

    print ('Average of ', person[0], 'is ', average)
