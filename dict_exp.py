age = {"Adam" : 30 , "Bob" : 31 , "Chris" : 32 , "Dennis" : 33}
age["Tom"] = 34
print(age)
name = age.keys()
print(type(name))
print(name)
ages  = age.values()
print(ages)
age["Nick"] = 36
print(age.keys())
