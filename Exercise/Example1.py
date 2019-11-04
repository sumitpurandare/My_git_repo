#Question 1: Accept two int values from the user and return 
#their product. If the product is 
#greater than 1000, then return their sum


inp1 = int(input("Enter a first digit :"))
inp2 = int(input("Enter a second digit :"))
product = inp1*inp2
print("Product of two given number is --> ", product)
if product > 1000:
    sum = inp1 + inp2 
    print("Addition of given input digit is --> " ,sum)
