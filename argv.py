#Argument Variable 
#Complied by : Sumit Purandare
from sys import argv
user_name,script = argv
prompt = '> '
print(f"Hi {user_name} and this is {script} ")
print(f"i'd like to ask you some questions")
print(f"Do you like me {user_name}")
likes = input(prompt)
print(f"Where do you live,{user_name}")
lives=input(prompt)
print(f"What computer do you have {user_name}")
computer = input(prompt)
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")