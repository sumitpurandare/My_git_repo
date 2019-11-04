#Question 2: Given a range of numbers. Iterate from o^th number
# to the end number and print the sum of the current number 
# and previous number

def sumnum(num):
    previousnum = 0
    for i in range(num):
        sum = previousnum + i
        print(sum)
        previousnum =   i

sumnum(10)