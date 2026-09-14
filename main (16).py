import string 
import random 
string1 = list(string.ascii_lowercase)
string2 = list(string.ascii_uppercase)
string3 = list(string.digits)
string4 = list(string.punctuation)
characters_number = input("How many characters for the password:")
while True:
    try:
         characters_number = int(characters_number)
         if characters_number<6:
             print("you need at least 6 characters")
             characters_number = input("please enter the number again :")
         else:
            break
    except ValueError:
        print("please enter numbers only")
        characters_number = input("please enter the number again :")
random.shuffle(string1)
random.shuffle(string2)
random.shuffle(string3)
random.shuffle(string4)
part1 = round(characters_number*(30/100))
part2 = round(characters_number*(20/100))
password= []
for i in range(part1):
    password.append(string1[i])
    password.append(string2[i])
for i in range(part2):
    password.append(string3[i])
    password.append(string4[i])
random.shuffle(password)
password = "".join(password [0:])
print(password )
        
    






         
         
         