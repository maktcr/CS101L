########################################################################
##
## CS 101 Lab
## Program 8
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : write a program that allows the user to interact with a menu to add, remove, clear, or display test and program scores
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING:  menu choice must be valid option, returns message with valid choices if invalid input is given.
##                  all score inputs must be a number(float) and greater than 0, notifies user if invalid score given.            
##                  when displaying scores, if no scores are present and thus no calculations, prints n/a in its place
## OTHER COMMENTS: 
##      
##      
########################################################################

import math
import statistics

def get_prompt():
    print('\n{:>10}'.format('Grade Menu'))
    print('\n1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Test')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignment')
    print('D - Display Scores')
    print('Q - Quit\n')
    return input('==> ').upper()

def add_test_score():   
    try:
        score = float(input('Enter the new Test score 0-100 ==> '))
        if score <= 0:
            print('Could not add score\n')
        else:
            testscores.append(score)
    except ValueError:
        print('Please enter a valid score')

def remove_test_score():
    try:
        score_to_remove = float(input('\nChoose Test score to remove ==> '))
        if score_to_remove in testscores:
            testscores.remove(score_to_remove)
            print('Test score {} removed'.format(score_to_remove))
        else:
            print('Could not remove score')
    except ValueError:
        print('Please enter a valid score')

def add_ass_score():
    score = float(input('Enter the new Assignment score 0-100 ==> '))
    if score <= 0:
        print('Could not add score\n')
    else:
        assignmentscores.append(score)

def remove_ass_score():
    score_to_remove = float(input('\nChoose Assignment score to remove ==> '))
    if score_to_remove in assignmentscores:
        assignmentscores.remove(score_to_remove)
        print('Assignment score {} removed'.format(score_to_remove))
    else:
        print('Could not remove score')

def display_scores():
    testcount = len(testscores)
    progcount = len(assignmentscores)
    testmin,progmin = min(testscores,default= 'n/a'),min(assignmentscores,default='n/a')
    testmax,progmax = max(testscores,default= 'n/a'),max(assignmentscores,default='n/a')
    testavg,progavg = get_avg()
    teststd,progstd = get_std()
    weighted_score = get_weight_score(testavg,progavg)
    print('{:<18}{}{:>11}{:>10}{:>10}{:>10}'.format('Type','#','min','max','avg','std'))
    print('============================================================')
    print('{:<18}{}{:>11}{:>10}{:>10}{:>10}'.format('Tests',testcount,testmin,testmax,testavg,teststd))
    print('{:<18}{}{:>11}{:>10}{:>10}{:>10}'.format('Programs',progcount,progmin,progmax,progavg,progstd))
    print('\nThe weighted score is {}'.format(weighted_score))

def get_avg():
    try: testavg = '{:.2f}'.format(math.fsum(testscores) / len(testscores))
    except ZeroDivisionError: testavg = 'n/a'
    try: progavg = '{:.2f}' .format(math.fsum(assignmentscores) / len(assignmentscores))
    except ZeroDivisionError: progavg = 'n/a'
    
    return testavg,progavg

def get_std():
    try: teststd = '{:.2f}'.format(statistics.stdev(testscores))
    except statistics.StatisticsError: teststd = 'n/a' 
    try: progstd = '{:.2f}'.format(statistics.stdev(assignmentscores))
    except statistics.StatisticsError: progstd = 'n/a'
    return teststd,progstd

def get_weight_score(test,prog):
    try: score = (test * 0.6) + (prog * 0.4)
    except TypeError: score = '0.00'
    return score

testscores = []
assignmentscores = []

running = True
while running:

    choice = get_prompt()

    if choice == '1' :
        add_test_score()
    elif choice == '2' :
        remove_test_score()
    elif choice == '3' :
        testscores.clear()
    elif choice == '4' :
        add_ass_score()
    elif choice == '5' :
        remove_ass_score()
    elif choice == '6' :
        assignmentscores.clear()
    elif choice == 'D' :
        display_scores()
    elif choice == 'Q' :
        print('Goodbye')
        running = False
    else:
        print('\nPlease enter a valid option\n')