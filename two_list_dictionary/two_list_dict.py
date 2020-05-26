# My solution
def two_list_dictionary(list1, list2):
    new_dict = {}
    i = 0

    while i < len(list1):
        if i < len(list2):
            new_dict[list1[i]] = list2[i]
        else:
            new_dict[list1[i]] = None
        i += 1

    return new_dict

two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
