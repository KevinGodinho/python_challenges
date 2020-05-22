# My solution
def list_check(l):
    for i in l:
        if not type(i) == list: return False
    return True

list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True

# Explanation:

# if any value in list is not type list return False
# else return True


# Instructor's solution
# def list_check(vals):
#     return all(type(l) == list for l in vals)
