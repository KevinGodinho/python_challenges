# My solution
def find_the_duplicate(l):
    dup_dict = {}

    for key in l:
        if key in dup_dict:
            dup_dict[key] += 1
        else:
            dup_dict[key] = 1

        if dup_dict[key] > 1:
            return key

    return None


print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None


# Instructor's solution
# def find_the_duplicate(arr):
#     counter = {}
#     for val in arr:
#         if val in counter:
#             counter[val] += 1
#         else:
#             counter[val] = 1
#     for key in counter.keys():
#         if counter[key] > 1:
#             return int(key)
