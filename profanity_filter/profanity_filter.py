import re

def censor(text):
    pattern = re.compile(r'\bfrack\w*\b', re.I)
    result = pattern.sub('CENSORED', text)
    return result


print(censor('Frack you'))
print(censor('I hope you fracking die'))
print(censor('you fracking Frack'))
