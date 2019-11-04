import random
def password(length):
    pwd = str()
    char = "abcdefghijklmnoprstuvwxyz1234567890!@#$%^&*()"
    for x in range(length):
        pwd = pwd + random.choice(char)
    return pwd
print("Get now password of 10 character consists of special character ,numneric and alphabets :\n",password(10))
    