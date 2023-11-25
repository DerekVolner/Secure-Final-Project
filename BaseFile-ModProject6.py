'''
Class: 44-141 Computer Programming I

Author: Derek Volner

Description: project for encrypting a file input by user then decrypting the file to a different output file

Due: 4/21/2022

I pledge that I have completed the programming assignment independently.

I have not copied the code from a student or any source.

I have not given my code to any other student and will not share this code

with anyone under any circumstances. '''
#Functions
def encrypt():
    users_file=input("Enter file to encrypt:")
    base_file=open(users_file, "r")
    users_file_encryption=input("Enter output file:")
    Encrypted_file=open(users_file_encryption,"w")
    read=[]
    rest=[]
    #puts the characters of base_file into a singular list
    for letter in base_file:
        read+=list(letter)
    #appends the string value of the character to rest list after it's ascii value is subtracted from it's index value in the read list
    for x in read:
        rest.append(str((ord(x))-read.index(x))+".") 
        read.remove(x)
        read.insert(0,'y')
    #writes the contents of the rest list to the output file
    for y in rest:
        Encrypted_file.write(y)
    #closes both output and input files and returns a print statement of the str and the value the user inputted for users_file_encryption at the start 
    base_file.close()
    Encrypted_file.close()
    return print("Encrypted passwords wrote to "+ users_file_encryption)

def decrypt():
    encrypted=input("Enter file to decrypt:")
    altered_file=open(encrypted, "r")
    decrypted=input("Enter output file:")
    decrypted_file=open(decrypted,"w")
    encrypted_list=[]
    decryptinglist=[]
    #splits the encrypted file into single value strings
    for letter in altered_file:
        m=letter.split(".")
        encrypted_list+=m
    #Takes the value of x and adds its index back to the value to return the character, then removes and replaces the index position with str (y)
    #and continues when x reaches ''    
    for x in encrypted_list:
        y=encrypted_list.index(x)
        if (x==''):
            continue
        z=int(x)
        decryptinglist.append(chr(((z))+y))
        encrypted_list.remove(x)
        encrypted_list.insert(0,'y')
    #writes the decrypting list to the output file    
    for character in decryptinglist:
        decrypted_file.write(character)
    #closes both output and input files and returns a print statement of the str and the value the user inputted for decrypted at the start of function
    altered_file.close()
    decrypted_file.close()
    return print("Decrypted passwords wrote to "+ decrypted)

#Main Program
#variables
print("Welcome to the password encryption program!")
user_input=input("Options:\n< e for encryption >\n< d for encryption >\n< q to exit>\nSelect an option:")

#While Loop
while (user_input!="q"):
    if (user_input=="e"):
        encrypt()
    if (user_input=="d"):
        decrypt()
    user_input=input("Options:\n< e for encryption >\n< d for encryption >\n< q to exit>\nSelect an option:")
print("Thank you for using our program!")