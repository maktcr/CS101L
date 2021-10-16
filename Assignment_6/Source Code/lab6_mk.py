########################################################################
##
## CS 101 Lab
## Program 6?
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : write a program to encrypt and decrypt a string given by the user
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING:
##      
##
## OTHER COMMENTS:
##      had to tweak the main() funtion a bit to accept my encode/decode 'solution.' Couldnt seem to find an easier way.
##      
########################################################################
import string 

def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.''' 
    for i in string_text:
        if i == ' ':
            print(' ',end = '')
        else:
            print(chr(ord(i)+int_key),end = '')
    
def Decrypt(string_text, int_key): 
    ''' Decrypts Caesar-encrypted string with specified key. '''
    for i in string_text:
        if i == ' ':
            print(' ',end = '')
        else:
            print(chr(ord(i)-int_key),end = '')
            
def Get_input(): 
    '''Interacts with user. Returns one of: '1', '2', 'Q'.''' 
    num = str(input('Enter your selection ==> '))
    return num
  
def Print_menu():
    '''Prints menu. No user interaction. '''
    print('MAIN MENU:\n1) Encode a string\n2) Decode a string\nQ) Quit')
    
  
def main():
    
    Again = True 
    while Again: 
        print()
        Print_menu()
        Choice = Get_input()
        print()
        
        if Choice == '1': 
            Plaintext = input("Enter (brief) text to encrypt: ").upper() 
            Key = int(input("Enter the number to shift letters by: "))
            print("Encrypted: ", end = '')
            Encrypt(Plaintext, Key)
            print()
        elif Choice == '2': 
            Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
            Key = int(input("Enter the number to shift letters by: "))
            print("Decrypted: ", end = '')
            Decrypt(Ciphertext, Key)
            print()
        else: 
            print("Have an ordinary day.") 
            Again = False 
      
      
# our entire program: 
main() 
