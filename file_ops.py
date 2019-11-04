filename = "file1.txt"
print("Enter Your name : ")
name = input()
print("Hi!" , name ,"Write something on file1")
file_wrt = input()
f = open("file1.txt","w")
var = f.write(file_wrt)
wrt = open(filename,"r")
print(wrt)
print("file has been updated go to C:\\Users\\SUMJEET\\Desktop\\Python" )
#print("Do you want to append more ? Enter Y for YES N for NO ")
inp1 = input ("Do you want to append more ? Enter Y for YES and N for NO \n >>")

if inp1 == "Y":
    print("Add something now ")
    append = input()
    f = open(filename,"a")
    var = f.write(append)
    print("file has been updated go to C:\\Users\\SUMJEET\\Desktop\\Python" )
else:
    exit
f.close()