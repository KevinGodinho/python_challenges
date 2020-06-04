# My solution
# I left print statements because they provided helpful output
# for troubleshooting values during each loop when writing this
def find_greater_numbers(l):
    if len(l) == 0:
        return 0

    count = 0
    
    right = len(l) - 1
    left = right - 1

    # loops = 1

    while True:
        # print(f'loops: {loops}')
        # loops += 1
        # print(f'left: {l[left]}, right: {l[right]}')
        # print(f'li: {left}, ri: {right}')

        if l[right] > l[left]:
            count += 1
            left -= 1
        else:
            left -= 1

        if left < 0:
            right -= 1
            left = right - 1

        if right == 0:
            return count

        # print(f'count: {count}')
        # print('-------------------------')

print(find_greater_numbers([1,2,3])) # 3
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0
