# Return a new list with every second value removed
# My solution
def remove_every_other(l):
    i = 0
    new_list = []

    while i < len(l):
        new_list.append(l[i])
        i += 2

    return new_list


remove_every_other([1,2,3,4,5]) # [1,3,5]
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1]


# Instructor's solution
# def remove_every_other(lst):
#     for i,val in enumerate(lst):
    # return [val for i,val in enumerate(lst) if i % 2 == 0]
