#Tuple
tuple = (1,2,3,4,4,4,4,4,4,4)
spam= len(tuple)
print(spam)
print("Old tuple is :", tuple)
tup_1 = tuple + (9,11)
print("New tuple value is :" , tup_1)
#coordinate and data type
x=12.36
y =23.56
coordinate = (x,y)
data_type = type(coordinate)
print(data_type)
print(coordinate)

coordinates = [(1,1),(2,4),(3,9),(4,16)]
for (x,y) in coordinates:
    print(x,y)

sum1 = sum(tuple)
print(sum1)

count1 = tuple.count(4)
print(count1)

