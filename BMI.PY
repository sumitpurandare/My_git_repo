print ("*******BMI Calculator*********")
print(" Compiled by : Sumit Purandare")
print ("Please provide weight and height as Input")
weight = float(input('Enter your weight in Kgs:  '))
height = float(input('Enter you height in CM :  '))
BMI= (weight/(height**2))*10000
if BMI < 18.5:
    print("You are underweight")
elif BMI < 24.5:
    print("Your BMI is in normal range,Congrats!!")
elif BMI  >  24.9:
    print("You are obese")
print ("BMI :",BMI)
print("BMI is between 18.5-24.9 --> NORMAL RANGE ") 