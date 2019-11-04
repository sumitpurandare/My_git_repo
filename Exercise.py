import numpy as np
zero_vector = []
zero_matrix = []
def funct():
    array_num()
    zero_vector = np.zeros(3)
    zero_matrix = np.zeros(5)
    print(zero_vector)
    print(zero_matrix)    
def array_num():
    x = np.array([[1,2,3,4],[5,6,7,8]])
    y = np.array([[10,20,50,60],[30,40,80,90]])
    P = np.transpose(x)
    Q = np.transpose(y)
    print("Transpose matrix : ",P)
    print ("Transpose matrix : ", Q)
    add = x + y 
    sum = P + Q
    print(" Addition of original array :", add)
    print("Addition of transpose array :" , sum)
    print("New output",P[1:3])
    print("return1:" , x[:,1]+y[:,1])
    print("return2:" , x[0:,]+y[0:,])
    print("add one ", add + 1)
   
    
funct()
