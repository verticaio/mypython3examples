list1 = [1, 2, 3, 4, 1]
list2 = [1, 2, 5]
print(set(list1))
print(set(list2))
print(list(set(list1) - set(list2)))
print(list(set(list2) - set(list1)))