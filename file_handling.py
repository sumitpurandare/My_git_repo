#file handing to read and write in the .txt file
#Complied by : Sumit Purandare

def main():
    txt = open("argv_1.txt","a+")
    for i in range (2):
        txt.write("Append text :\n")
        i=i+1
        
    #f = open("argv_1.txt","w+")
   # for i in range(10):
        #f.write("This is line %d\n" % (i+1))
    txt.close()
main()

