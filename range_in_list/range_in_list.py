# My solution
def range_in_list(data, start=0, end=0):
    new_end = end

    if end > len(data) or end == 0:
        new_end = len(data)

    return sum(data[start:new_end+1])

range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
