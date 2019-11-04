#list or array formation in Pyhton
#file name: List.py
#complied by : Sumit Purandare
#==================================================#
print("Below is list ")
spam=["cat","Dog","Sheep","Crocodile","Lion","Monkey"]
print("index 0 is ", spam[0])
spam1=[["Black","Red","Orange"],[100,200,300],[1.0,2.0,3.0]]
print(spam1[0][1])
print(spam1[1])
print(spam1[2])
print(spam[-1])
print(spam[1:2])
print(spam1[::2])
print(len(spam))
print(len(spam1))
concat=spam+spam1
print("Concatenation:\n",concat)
del spam[2]
print(spam)
del spam[2]
print(spam)
del spam[2]
print(spam)
del spam[2]
print(spam)
del spam[1]
print(spam)
for i in [0,1,2,3,4,5]:
    print(i)
spam.sort()
print(spam)