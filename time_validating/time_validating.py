import re

def is_valid_time(time):
    pattern = re.compile(r'(\d{1}|\d{2}):\d{2}')
    # another way to do this pattern is r'^\d\d?:\d\d$'
    if pattern.fullmatch(time):
        return True
    return False

print(is_valid_time('10:45'))
print(is_valid_time('1:23'))
print(is_valid_time('10.45'))
