#File handling Simple program
#Compiled by : Sumit Purandare
def main():
    txt=open("file.txt","r")
    spam=txt.read()
    print(spam)
    txt.close()
main()