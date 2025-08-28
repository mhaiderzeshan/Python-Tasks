"""
Implement a function that takes two sorted lists and merges them into one
sorted list without using sort() or sorted() .
"""


def merged_lists(list1, list2):
    list_merged = list1 + list2
    sorted_list = []
    while list_merged:
        small = min(list_merged)

        sorted_list.append(small)

        list_merged.remove(small)

    return sorted_list


list1 = [3, 4, 1, 9]
list2 = [2, 6, 7, 8, 4]
print(merged_lists(list1, list2))
