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
def encrypt2(plaintext, encrypted):
    try:
        base_file=open(plaintext, "r",encoding="utf-8")
        Encrypted_file=open(encrypted,"w",encoding="utf-8")
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
        return "Encrypted passwords wrote to "+ encrypted
    except(FileNotFoundError):
        return "The text file you specified cannot be found"
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
def decrypt2(encrypted, decrypted):
    try:
      altered_file=open(encrypted, "r",encoding="utf-8")
      encryptedList =[]
      decryptedList=[]
      splitter(altered_file, encryptedList)
      #above needed for splitter function
      decrypted_file=open(decrypted,"w",encoding="utf-8")
      process(encryptedList, decryptedList)
      for character in decryptedList:
        decrypted_file.write(character)

      altered_file.close()
      decrypted_file.close()
      return "Decrypted passwords wrote to "+ decrypted
    except(ValueError):
        return "The values in the file have not been encrypted with this program"
    except(FileNotFoundError):
        return "The text file you specified cannot be found"
            
def main():
    print("Welcome to the password encryption program!")
    user_input=input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit>\nSelect an option:")
    #While Loop
    while (user_input!="q"):
        if (user_input=="e"):
            users_file=input("Enter file to encrypt:")
            users_file_encryption=input("Enter output file:")
            print(encrypt2(users_file, users_file_encryption))
        if (user_input=="d"):
            encrypted=input("Enter file to decrypt:")
            decrypted=input("Enter output file:")
            print(decrypt2(encrypted, decrypted))
        user_input=input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit>\nSelect an option:")
    print("Thank you for using our program!")
    
if __name__ == "__main__":
    main()