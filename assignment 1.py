my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

my_list.append(6)
print("List after adding 6:", my_list)

my_list.remove(2)
print("List after removing 2:", my_list)

my_list[0] = 10
print("List after modifying first element to 10:", my_list)

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("\nInitial Dictionary:", my_dict)

my_dict['occupation'] = 'Engineer'
print("Dictionary after adding occupation:", my_dict)

del my_dict['age']
print("Dictionary after removing age:", my_dict)

my_dict['city'] = 'Los Angeles'
print("Dictionary after modifying city to Los Angeles:", my_dict)

my_set = {1, 2, 3, 4, 5}
print("\nInitial Set:", my_set)

my_set.add(6)
print("Set after adding 6:", my_set)

my_set.remove(3)
print("Set after removing 3:", my_set)

my_set.add(2)
print("Set after trying to add duplicate 2:", my_set)
