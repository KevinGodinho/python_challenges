import re

def parse_date(text):
    pattern = re.compile(r'(?P<d>[0-3][0-9])[,/.](?P<m>[0-1][0-9])[,/.](?P<y>\d{4})')
    match = pattern.fullmatch(text)
    if match:
        return {'d': match.group('d'), 'm': match.group('m'), 'y': match.group('y')}
    return None

print(parse_date('01/22/1999'))
print(parse_date('12,04,2003'))
print(parse_date('12.11.2003'))
print(parse_date('12.11.200312'))
