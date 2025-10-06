import random
import string
print("Password Generator")
l=int(input("Enter password length "))
cha=string.digits +string.ascii_letters +string.digits
pas="".join(random.choice(cha)for i in range(l))
print("your password ",pas)