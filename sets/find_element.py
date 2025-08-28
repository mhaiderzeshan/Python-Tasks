list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 5, 6]

set1 = set(list1)
set2 = set(list2)

find_element = set1.symmetric_difference(set2)
print(find_element)

