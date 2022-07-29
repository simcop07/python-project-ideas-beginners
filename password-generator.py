import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!\"$%&/*+àèìòù@#"

psw_number = int(input("How many passwords should I print? "))
psw_length = int(input("How long should the passwords be? "))

for i in range(psw_number):
    psw = ""
    for i in range(psw_length):
        psw += random.choice(characters)
    print(psw)
