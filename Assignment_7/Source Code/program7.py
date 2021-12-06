########################################################################
##
## CS 101 Lab
## Program 7
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : scan over a list of cars and output a list based on user input
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING: minimum mpg must be greater than 0 and less than 100
##                  proper file must be given
##
## OTHER COMMENTS:
##      
##      
########################################################################

def get_min_mpg():
    while True:
        try:
            mpg = float(input('Enter the minimum mpg -> '))
            if mpg <= 0:
                print('Fuel economy given must be greater than 0')
            elif mpg > 100:
                print('Fuel economy must be less than 100')
            else:
                return mpg

        except ValueError:
            print('You must enter a number for the fuel economy')

def open_file():
    while True:
        filename = input('Enter the name of the input vehicle file -> ')
        try:
            with open(filename,'r') as read_file:
                return [[x.strip() for x in line.strip().split('\t')] for line in read_file.readlines()]
        except FileNotFoundError:
            print('Could not open file',filename)
        except IOError:
            print('There is an IO Error',filename)


def output_to_file(minmpg,input_file):

        filename = input('Enter the name of the file to output to -> ')
        try:
            with open(filename,'w') as output_file:

                for line in input_file:
                    try: 
                        if minmpg >= float(line[7]): 
                            output_file.write('{:<5}{:<20}{:<20}{:>20}\n'.format(line[0],line[1],line[2],line[7]))

                    except TypeError: print("Couldn't convert value {} for vehicle {} {} {}" .format(line[7],line[0],line[1],line[2]))

        except IOError: print('There is an IO Error',filename)

#main
minmpg = get_min_mpg()
input_file = open_file()[1:]
output_to_file(minmpg,input_file)

