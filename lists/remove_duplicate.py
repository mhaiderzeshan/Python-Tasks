user_input = (input("Enter the list of integers: "))
my_list = list(map(int, user_input.split()))
my_dict = {}

for item in (my_list):
    my_dict[item] = item

final_list = list(my_dict.values())
print(final_list)

