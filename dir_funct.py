name1 = "this is a string"
name2 = 1234 #this is an integer
cast1 = type(name1)
cast2 = type(name2)
spam1 = dir(name1)
spam2 = dir(name2)
print(cast1)
print(cast2)
print("All string operaion :\n " ,spam1)
print("All integer operaion :\n" ,spam2)
dir(str)
que = name1.upper()
print(que)