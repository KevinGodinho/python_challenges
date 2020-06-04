# My solution
def is_odd_string(s):
    l = s[0:]

    ascii_total = 0

    for letter in l:
        ascii_total += ord(letter)

    return bool(ascii_total % 2)


is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
