#User input and open txt file from function\\
#Complied by : Sumit Purandare
from sys import argv
script, filename = argv
txt = open(filename)
print(f"Name of the file is {filename} :")
print(txt.read)
print(f"Name of the file is {filename}")
file_again=input("> ")
txt_again =  open(file_again)
print(txt_again.read())