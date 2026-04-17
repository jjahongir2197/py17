import random
import string

def generate_password(length):

    chars = string.ascii_letters + string.digits

    password = ""

    for i in range(length):
        password += random.choice(chars)

    return password


l = int(input("Length: "))

print("Password:", generate_password(l))
