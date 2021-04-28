# Assignment 3:
"""
There is a list shown below titled original_list.
Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.
IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.
"""

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]

# your code below:
first_nr = original_list[3][0]
second_nr = original_list[3][1]
third_nr = original_list[3][2]
aux_list = [first_nr, second_nr, third_nr]
aux_list.sort()
new_tuple = (aux_list[0], aux_list[1], aux_list[2])

#new_list = [original_list[:3], new_tuple]
new_list = [original_list[0], original_list[1], original_list[2], new_tuple]
print(new_list)
