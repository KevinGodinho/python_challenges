import re

def parse_bytes(text):
    pattern = re.compile(r'[0-1]{8}')
    return pattern.findall(text)

print(parse_bytes('11010101'))
