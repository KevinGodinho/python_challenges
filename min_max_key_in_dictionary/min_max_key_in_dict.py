# My first solution
def min_max_key_in_dictionary(d):
    return [min(d),max(d)]

# My solution trying not to use built in functions
def min_max_key_in_dictionary(d):
    max = 0
    min = 0
    
    for key in d:
        if min == 0 and max == 0:
            max = key
            min = key

        if key > max:
            max = key

        if key < min:
            min = key

    return [min,max]


min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
