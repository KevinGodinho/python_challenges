# My first solution
# def two_oldest_ages(l):
    # oldest = max(l)
    # l.remove(oldest)
    #
    # second_oldest = max(l)
    #
    # return [second_oldest, oldest]


# My second solution
# Just solved using loop, different logic
# First solution is probably better
# def two_oldest_ages(l):
#     oldest_list = []
#
#     while len(oldest_list) < 2:
#         oldest = max(l)
#         l.remove(oldest)
#
#         oldest_list.append(max(l))
#         oldest_list.append(oldest)
#
#     return oldest_list


# My third solution
# This might be the best one
# def two_oldest_ages(l):
#     sorted_list = sorted(l)
#
#     return sorted_list[-2:]


# My fourth solution
# The third one got me thinking..
def two_oldest_ages(l):
    return sorted(l)[-2:] # was able to complete in one line


two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
