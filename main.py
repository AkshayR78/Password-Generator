import random
import string

print("This is a random password generator")
charlen = int(input("Enter the required number of characters:"))
print("Choose the characters from which the password must be created:")
print("1.Letters, 2.Numbers, 3. Exit")
characterlist=""

while(True):
    choice=int(input("Pick a number:"))
    if(choice == 1):
        characterlist = characterlist+string.ascii_letters
        break
    if(choice == 2):
        characterlist = characterlist+string.digits
        break
    if(choice == 3):
        break
    else:
        print("Enter a valid choice/option")
password =[]
for i in range(charlen):
    randchar=random.choice(characterlist)
    password.append(randchar)
print("Your random password is:")
print(password)