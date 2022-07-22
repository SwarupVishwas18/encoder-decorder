"""
    Name : Swarup Deepak Vishwas
    Project : Encrypter and Decrypter
"""

from colorama import Fore,Back

print()
print()
print(Fore.CYAN+"--------------------------------------------------")
print(Fore.GREEN+"           ENCRYPTER AND DECRYPTER")
print(Fore.CYAN+"--------------------------------------------------")
print()
print()

# Encrypting Function

def encrypter():
    data = input("Enter the Data : ")
    str = []
    for i in data:
        str.append(chr(ord(i)+5))
    s = ''.join(str)
    print("Encrypted Data is : ",end=" ")
    print(Fore.BLUE,end=" ")
    print(s)

def decrypter():
    data = input("Enter the Data : ")
    str = []
    for i in data:
        str.append(chr(ord(i)-5))
    s = ''.join(str)
    print("Decrypted Data is : ",end=" ")
    print(Fore.BLUE,end=" ")
    print(s)

while True:
    print(Fore.MAGENTA+" 1. Encrypt Data")
    print(Fore.MAGENTA+" 2. Decrypt Data")
    print(Fore.RED+" 3. Exit")
    print(Fore.GREEN)
    ch = input("Enter Your Choice : ")

    if(ch=="1"):
        encrypter()
    elif(ch=="2"):
        decrypter()
    elif(ch=='3'):
        print(Fore.YELLOW+"Thanks For Visiting!!")
        exit()
    else:
        print(Fore.RED+"Enter Valid Option!!")
    print(Back.RESET)
    print(Fore.CYAN+"--------------------------------------------------")
    print(Fore.CYAN+"--------------------------------------------------")
    
