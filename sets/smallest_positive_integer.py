list1 = [-3, -5, 0, 1, 3, 2, 5]
set1 = set(list1)

i = 1
while True:
    if i not in set1:
        print(i)
        break
    i += 1
