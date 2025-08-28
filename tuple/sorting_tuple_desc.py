"""
1-  make a function
2- takes a tuple of tuples
3- sort them in desc order by second element
4- break ties with first element in asc
"""
data = ((1, 3), (3, 3), (4, 2), (1, 4))


def sorting_tuple(data):
    sorted_data = sorted(data, key=lambda x: (x[0], -x[1]))

    print(sorted_data)


print(sorting_tuple(data))
