# My solution
def sum_up_diagonals(l):
    total = []

    for (i,arr) in enumerate(l):
        total.append(arr[i])
        total.append(arr[-1-i])

    return sum(total)


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
sum_up_diagonals(list2) # 30

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]
sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
sum_up_diagonals(list4) # 68
