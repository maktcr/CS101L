########################################################################
##
## CS 101 Lab
## Program 4
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : Making a program that plays a slot game
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING:
##      
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes (or no) '''
    while True:
        playagain_input = input('Play again? Y/Yes for yes. N/No for no.')
        playagain = playagain_input.lower()
        if (playagain == 'y' or playagain == 'yes'):
            return True
        elif (playagain == 'n' or playagain == 'no'):
            return False
        else:
            print('Please enter Y or Yes for "yes", N or No for "no."')
            continue
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        numchips = int(input('Enter your wager amount : '))
        if numchips <= 0:
            print('You cannot wager 0 chips or less!')
            continue
        elif numchips > bank:
            print('You cannot wager more chips than you have!')
            continue
        else:
            return numchips          

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reelone = random.randint(1,10)
    reeltwo = random.randint(1,10)
    reelthree = random.randint(1,10)
    return reelone, reeltwo, reelthree

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb == reelc:
        return 3
    elif (reela == reelb or reela == reelc or reelb == reelc):
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        dabank = int(input('How many chips would you like to play with?'))
        if dabank <= 0 or dabank > 100:
            print('How many chips would you like to play with? Enter a value between 1 and 100 : ')
            continue
        else:
            return dabank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        bank_start = bank
        maxamount = bank
        spin = 0
        
        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > maxamount:
                maxamount = bank
            spin += 1
            
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print('You lost all {} in {} spins'.format(bank_start,spin))
        print("The most chips you had was", maxamount)
        playing = play_again()
