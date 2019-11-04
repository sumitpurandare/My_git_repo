#The copy Module’s copy() and deepcopy() Functions

import copy
spam=["Watch","Table","Bottle"]
spam1=copy.copy(spam)
spam1[1]=65
print(spam1)