########################################################################
##
## CS 101 Lab
## Program #3
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : Write a program to figure out the number guessed by the player
##          
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING: remainder must be greater than 0, and less than the number being divided by
##                  example: remainder_three value must be greater than 0 and less than 3
##
## OTHER COMMENTS:
##      
##
########################################################################

print('Welcome to Flarsheim Guesser')

choice = 'y'

while (choice == 'Y' or choice == 'y'):
    print('\nPlease think of a number between and including 1 and 100')

    remainder_three = 0
    remainder_five = 0
    remainder_seven = 0

    remainder_three = int(input('\nWhat is the remainder when your number is divided by 3? '))
    while(remainder_three < 0 or remainder_three >= 3):
        if remainder_three < 0:
            print('The value entered must be 0 or greater')
        elif remainder_three >= 3:
            print('The value entered must be less than 3')

        remainder_three = int(input('What is the remainder when your number is divided by 3?'))
        
    remainder_five = int(input('\nWhat is the remainder when your number is divided by 5?'))
    while(remainder_five < 0 or remainder_five >= 5):
        if remainder_five < 0:
            print('The value entered must be 0 or greater')
        elif remainder_five >= 5:
            print('The value entered must be less than 5')

        remainder_five = int(input('What is the remaider when your number is divided by 5?'))


    remainder_seven = int(input('\nWhat is the remainder when your number is divided by 7?'))
    while(remainder_seven < 0 or remainder_seven >= 7):
        if remainder_seven < 0:
            print('The value entered must be 0 or greater')
        elif remainder_seven >= 7:
            print('The value entered must be less than 5')

        remainder_seven = int(input('What is the remaider when your number is divided by 7?'))

    for i in range(1,101):
        if(i % 3 == remainder_three and i % 5 == remainder_five and i % 7 == remainder_seven):
            print('Your number was {}'.format(i))
            print('how cool was that\n')

    choice = input('Do you want to play again? Y to continue\nN to quit ==>')
    while(choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n'):
        choice = input('Do you want to play again? Y to continue, N to quit ==>')
        

        
