data = ((1, 3), (3, 3), (4, 2), (1, 4))


def sorting_tuple(data):
    sorted_data = sorted(data, key=lambda x: (x[0], -x[1]))

    print(sorted_data)


print(sorting_tuple(data))
