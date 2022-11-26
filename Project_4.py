"""Create a program that takes the length of the password as input and generates a random password of the same length.
The strength of the password depends equally on the 4 properties mentioned below.
If the password generated randomly following the rules or constraints given below,
then that password is treated as good in terms of strength and accepted otherwise ignore that password.
The properties to be followed for a strong password are:
At least 12 characters.
A mixture of both uppercase and lowercase letters.
A mixture of letters and numbers.
Inclusion of at least one special character, e.g., @ #?]"""



import random
print("Your required password length must be greater than 12")
MAX_LEN=int(input("Length of password:- "))
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 

                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',

                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',

                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 

                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',

                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',

                     'Z']
 

SYMBOLS = ['!','@', '#', '$', '%','^',"&",'_',';', '=', ':', '?', '.', '/', '|', '~', '*']
 

xdig=random.choice(DIGITS)
xupper=random.choice(UPCASE_CHARACTERS)
xlower=random.choice(LOCASE_CHARACTERS)
xsym=random.choice(SYMBOLS)
temp_pass=xdig+xupper+xlower+xsym

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
if MAX_LEN>=12:
    for i in range(MAX_LEN-4):
        temp_pass=temp_pass+random.choice(COMBINED_LIST)
    print("********YOUR GENERATED PASSWORD IS************")
    print(temp_pass)
else:
    print("password length must be greator than 12")