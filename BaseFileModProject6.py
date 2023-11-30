'''
Class: 44382-01 Secure Programming

Author: Derek Volner

Description: project for adding security measures to basic encryption and decryption project from computer programming 1

Due: 12/1/2023

I pledge that I have completed the programming assignment independently.

I have not copied the code from a student or any source.

I have not given my code to any other student and will not share this code

with anyone under any circumstances. '''
#Functions
#puts the characters of base_file into a singular list
def putter(base, read):
    for letter in base:
        read+=list(letter)  
"""Converter appends the string value of the character to rest list after it's ascii value 
 is subtracted from it's index value in the read list"""
 
def Converter(rest, read):
    for x in read:
        if(x!="y"):
            rest.append(str((ord(x))-read.index(x))+".") 
            read.remove(x)
            read.insert(0,'y') 
        elif (x=="y"):
             rest.append(str((ord(x))-read.index(x))+"a"+".")
             read.remove(x)
             read.insert(0,'y')
def encrypt():
    try:
        users_file=input("Enter file to encrypt:")
        base_file=open(users_file, "r")
        users_file_encryption=input("Enter output file:")
        Encrypted_file=open(users_file_encryption,"w")
        read=[]
        rest=[]
        putter(base_file, read)
        Converter(rest, read)
        
        #writes the contents of the rest list to the output file
        for y in rest:
            Encrypted_file.write(y)
        #closes both output and input files and returns a print statement of the str and the value the user inputted for users_file_encryption at the start 
        base_file.close()
        Encrypted_file.close()
        return print("Encrypted passwords wrote to "+ users_file_encryption)
    except(FileNotFoundError):
        print("The file you specified cannot be found")
#splits the encrypted file into single value strings
def splitter(altered, eList):
    for letter in altered:
         m=letter.split(".")
         eList+=m
#Takes the value of x and adds its index back to the value to return the character, 
# then removes and replaces the index position with str (y)
#and continues when x reaches ''    
def process(eList, dList):
      for x in eList:
        y=eList.index(x)
        if (x==''):
            continue
        if(x=="121a"):
            z=int (121)
            dList.append(chr(z))
            eList.remove(x)
            eList.insert(0,'y')
        elif(x!="121a"):
            zy=int(x)
            dList.append(chr(((zy))+y))
            eList.remove(x)
            eList.insert(0,'y')
def decrypt():
    try:
        encrypted=input("Enter file to decrypt:")
        altered_file=open(encrypted, "r")
        decrypted=input("Enter output file:")
        decrypted_file=open(decrypted,"w")
        encrypted_list=[]
        decryptinglist=[]
        splitter(altered_file, encryptedList)

        process(encryptedList, decryptedList)

        #writes the decrypting list to the output file    
        for character in decryptinglist:
            decrypted_file.write(character)
        #closes both output and input files and returns a print statement of the str and the value the user inputted for decrypted at the start of function
        altered_file.close()
        decrypted_file.close()
        return print("Decrypted passwords wrote to "+ decrypted)
    except(ValueError):
        return "The values in the file have not been encrypted with this program"
    except(FileNotFoundError):
        print("The file you specified cannot be found")

            
#Main Program
#variables
print("Welcome to the password encryption program!")
user_input=input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit>\nSelect an option:")

#While Loop
while (user_input!="q"):
    if (user_input=="e"):
        encrypt()
    if (user_input=="d"):
        decrypt()
    user_input=input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit>\nSelect an option:")
print("Thank you for using our program!")