# My solution
def same_frequency(num1,num2):
    num1_list = list(str(num1)[0:])
    num2_list = list(str(num2)[0:])

    if len(num1_list) != len(num2_list):
        return False

    dict1 = {}
    dict2 = {}

    for (i,num) in enumerate(num1_list):
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1

        if num2_list[i] in dict2:
            dict2[num2_list[i]] += 1
        else:
            dict2[num2_list[i]] = 1

    if dict1 == dict2:
        return True

    return False


print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True


# Instructor's solution
# def same_frequency(num1,num2):
#     d1 = {letter:str(num1).count(letter) for letter in str(num1)}
#     d2 = {letter:str(num2).count(letter) for letter in str(num2)}
#
#     for key,val in d1.items():
#         if not key in d2.keys():
#             return False
#         elif d2[key] != d1[key]:
#             return False
#     return True
