my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1,2,3,4,5]

# Create another list that contains the contents from each of these lists (the last three of each list)
my_list.sort()
my_list.reverse()

another_list.sort()
another_list.reverse()

final_list = my_list[2:] + another_list[2:]
print(final_list)

my_tuple = (1,2,3)
xpto = my_tuple[0]

new_tuple = my_tuple[:]
print(new_tuple)