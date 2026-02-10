import random
import string

print("PASSWORD GENERATOR")

l=int(input("Enter desired length of password: "))
chars=""
if input("Include letters (y/n)?  ").lower()=='y':
    chars+=string.ascii_letters
if input("Include digits (y/n)?  ").lower()=='y':
    chars+=string.digits
if input("Include symbols (y/n)?  ").lower()=='y':
    chars+=string.punctuation

if chars=="":
    print("Error: No character set selected")
else:
    password=""
    for i in range(l):
        password+=random.choice(chars)
        
        
    print("Generated password: ",password)
