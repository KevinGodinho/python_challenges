#My solution
def includes(col, val, i=0):

    if type(col) == str or type(col) == list:
        for (index, data) in enumerate(col):
            if index >= i and data == val:
                return True
        else: return False
    elif type(col) == dict:
        for key, v in col.items():
            if v == val:
                return True
        else: return False


# Instructor's solution
# def includes(item,val,start=None):
#     if type(item) == dict:
#         return val in item.values()
#     if start is None:
#         return val in item
#     return val in item[start:]


includes([1, 2, 3], 1) # True
includes([1, 2, 3], 1, 2) # False
includes({ 'a': 1, 'b': 2 }, 1) # True
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
