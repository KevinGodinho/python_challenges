# my first solution
# def truncate(string, n):
#     trunc = '...'
#
#     if n < 3: return 'Truncation must be at least 3 characters.'
#     if n == 3: return trunc
#     if len(string) < n: return string
#
#     new_string = []
#
#     for (index,char) in enumerate(string):
#         new_string.append(char)
#         if index == (n - len(trunc)) - 1: break
#
#     return f"{''.join(new_string)}{trunc}"


# my second solution, refactoring logic to shorten
def truncate(string, n):
    trunc = '...'

    if n < 3: return 'Truncation must be at least 3 characters.'
    if n == 3: return trunc
    if len(string) < n: return string

    truncated_string = f'{string[0:n-len(trunc)]}...'

    return truncated_string

# Instructor's solution
# def truncate(string, n):
#     if (n < 3):
#         return "Truncation must be at least 3 characters."
#     if (n > len(string) + 2):
#         return string
#
#     return string[:n - 3] + "..."


print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 1)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters."
print(truncate("Hello World", 6)) # "Hel..."
# (truncate("Problem solving is the best!", 10)) # "Problem..."
# truncate("Another test", 12) # "Another t..."
# truncate("Woah", 4) # "W..."
# truncate("Woah", 3) # "..."
# truncate("Yo",100) # "Yo"
# print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"
