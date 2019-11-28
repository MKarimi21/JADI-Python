# How many N character words are in a string
# you can use in data analysing in contex in lectures with this algarithm for O(?)


def nWordinString(string, n):
    numberofNwords = 0
    words = string.split()
    for this_word in words:
        # print ('this word is: ', this_word, len(this_word))
        if len(this_word) == n:
            # print('found one: ', this_word)
            numberofNwords = numberofNwords = 1
    return numberofNwords

string = input('What is your string?\n')

for n in range(1, 10):  # need max split string replace to 10
    n_words = nWordinString(string, n)
    print ('number of ', n, 'words is ', n_words)
