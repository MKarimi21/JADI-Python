# Reverse String Problem with 2 def

def reverse_str_v1 (s):
    r = ''
    for char in s:
        r = char + r
    return r

def reverse_str_v2 (s):
    r = ''
    for i in range (len(s)-1, -1,-1):
        r = r + (s[i])
    return r

input_str = input('Give me a string:\n')
reverse = reverse_str_v2(input_str)

print ('Your reverse string:\n', reverse)
