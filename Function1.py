#def my_animal(animal):
    #print(animal)

#fruits = ["Apple" , "Banana" , "Orange"]

#my_animal(fruits)


#def ops(x):
 #   return 5*x
#print (ops(3))
#print (ops(5))
#print (ops(7))


#***Factorial** 
#def facto(x):
 #   if x==1:
  #      return 1
   # else:
    #    return x*facto(x-1)
    
#print (facto(7))


def fabo(n):
    a=0
    b=1
    
    print (a)
    print(b)
    
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)
fabo(10)