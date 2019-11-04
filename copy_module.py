import copy
old_list = [[11,12,13],[14,15,16],[17,18,19]]
new_list = copy.copy(old_list)
print(new_list)
new_list [0] [1]= "S"
print(old_list)
print(new_list)
new_list1 = copy.deepcopy(old_list)
new_list1[0][1] = "E"
print(old_list)
print(new_list1)
print(id(new_list))
print(id(old_list))
print(id(new_list1))
