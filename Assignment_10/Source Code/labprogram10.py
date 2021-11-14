########################################################################
##
## CS 101 Lab
## Program 10
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : write a program that counts number of words in a text file; outputting top 10 words, unique words, and words used once
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING: will loop until valid text file is given
##
##
##
##
## OTHER COMMENTS: 
##      
##      
########################################################################

import string

def get_lst(file):
    list_of_words = []
    
    for line in file:
        for words in line.split():
            word = words.lower().strip()
            list_of_words.append(word)

    return list_of_words

def clean_list(list):
    clean_list = [''.join(char for char in word if char not in string.punctuation) for word in list if len(word) > 3]
    return clean_list

def get_unique_words(list):
    return len(set(list))   #set will ignore dupes, leaving only unique words

def words_used_once(c_list):
    word_dict = {}
    words_used_once = []
    for word in c_list:
        word_dict[word] = word_dict.get(word,0) + 1

    for key,value in word_dict.items():
        if value == 1:
            words_used_once.append(key)

    return len(words_used_once)

def print_stuff(list):

    word_dict = {}
    for word in list:
        word_dict[word] = word_dict.get(word,0) + 1
    sorted_dict = dict(sorted(word_dict.items(), key = lambda x:x[1] , reverse = True))   #builds dict of word,instances - key,value pairs, then sorts dict

    num = 1

    print('\n{:<11}{:<14}{}'.format('#','Word','Freq.'))
    print('='*30)
    for key,value in sorted_dict.items():
        if num <= 10:
            print('{:<11}{:<18}{:<}'.format(num,key,value))
            num += 1
        
running = True
while running:
    filename = input('Enter name of file to open => ')
    try: 
        file = open(filename,'r')
        running = False
    except FileNotFoundError: print('Could not open file {}\nPlease try again'.format(filename))
    
list_words = get_lst(file)
file.close()

clean_words = clean_list(list_words)           #removes punctuation and words with less than 3 characters

print_stuff(clean_words)

print('\nThere are {} words that occur only once' .format(words_used_once(clean_words)))
print('there are {} unique words\n' .format(get_unique_words(clean_words)))
