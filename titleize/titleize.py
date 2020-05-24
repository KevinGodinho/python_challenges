# my solution
def titleize(text):
    text_list = [char for char in text]
    new_list = []

    i = 0

    while i < len(text_list):
        if i == 0:
            new_list.append(text_list[i].capitalize())
        elif text_list[i] == ' ':
            new_list.append(text_list[i])
            i += 1
            new_list.append(text_list[i].capitalize())
        else:
            new_list.append(text_list[i])
        i += 1

    return ''.join(new_list)


# Instructor's solution
# def titleize(string):
#     return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
