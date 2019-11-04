list1 = [1,2,3,4]
list3 = [1,2,3,4]
list2 = list1
print(list1[0])
if list1 == list3:
    print ("True")
else:
    print ("False")
print(list2)
print(id(list1))
print(id(list3))
if id(list1) == id(list3):
    print ("True")
else:
    print("False")