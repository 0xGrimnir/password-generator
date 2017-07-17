import random

def passwd(length):
    pw = str()
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=?"
    for i in range(length):
        pw = pw + random.choice(char)
    return pw

#Let x = the length of your desired password.
print(passwd(x))
