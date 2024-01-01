import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

password = []

def pas(characterList):
    for i in range(length):

        # Picking a random character from our 
        # character list
        randomchar = random.choice(characterList)
        
        # appending a random character to password
        password.append(randomchar)

    # printing password as a string
    print("The random password is " + "".join(password))


characterList = ""
while(True):
    ch=int(input("Enter a number : "))
    if(ch==1):
        characterList += string.ascii_letters
        pas(characterList)
    elif(ch==2):
        characterList += string.digits
        pas(characterList)
    elif(ch==3):
        characterList += string.digits
        pas(characterList)
    elif(ch==4):
        break
    else:
        print("Enter a valid number")
        
