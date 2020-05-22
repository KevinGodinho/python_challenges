# My solution
def reverse_string(text):
    return ''.join([char for char in text][::-1])

reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'

# Explanation:

# Used list comprehension to loop through string argument converting it to list, each char its own index
# Attached slice method [::-1] to the end, which reverses the list
# Attached join method to beginning and specified no spaces, which converts back to string type


# Instructor's solution
# def reverse_string(str):
#     s = ''
#     for i, char in enumerate(str[::-1]):
#         s += char
#     return s
