########################################################################
##
## CS 101 Lab
## Program 9
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : write a program that allows the user to interact with a csv file containing crime report information
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING: program will loop until given a valid file name input and valid 'offense' input
##
##
##
##
## OTHER COMMENTS: 
##      
##      
########################################################################
import csv

def month_from_number(num):
    intg = int(num)
    monthlist = ['January','February','March','April','May','June','July','August','September','October','November','December']
    try: month = monthlist[intg - 1]
    except IndexError: 'number must be 1-12'
    return month

def read_in_file(filename):
    file = open(filename, encoding = 'utf-8')
    csv_file = csv.reader(file)

    list_of_lists = []
    for line in csv_file:
        list_of_lists.append(line)
    file.close()
    return list_of_lists

def create_reported_date_dict(list):
    dates_dict = {}
    for line in list[1:]:
        date = line[1].strip()
        dates_dict[date] = dates_dict.get(date, 0) + 1
    return dates_dict

def create_reported_month_dict(list):
    month_dict = {}
    for line in list[1:]:
        month = line[1].split('/')[0].strip()
        month_dict[month] = month_dict.get(month,0)+1
    return month_dict

def create_offense_dict(list):
    crime_dict = {}
    for line in list[1:]:
        crime = line[7].strip()
        crime_dict[crime] = crime_dict.get(crime,0)+1
    return crime_dict

def create_offense_by_zip(list):

    zip_dict = {}
    
    for line in list[1:]:
        crime = line[7].strip()
        zip_code = line[13].strip()
        if crime in zip_dict:
            if zip_code in zip_dict[crime]:
                zip_dict[crime][zip_code] += 1
            else:
                zip_dict[crime][zip_code] = 1
        else:
            zip_dict[crime] = dict()
            zip_dict[crime][zip_code] = 1   

    return zip_dict

def get_max_month(dict):
    maxmonthvalue = max(dict.values())
    maxmonthkey = max(dict, key=dict.get)
    month = month_from_number(maxmonthkey)

    return month,maxmonthvalue

def get_max_crimes(dict):
    maxcrimevalue = max(dict.values())
    maxcrimekey = max(dict,key=dict.get)
    
    return maxcrimekey,maxcrimevalue

if __name__ == '__main__' :
    file_is_invalid = True
    while file_is_invalid:
        try:
            filename = str(input('Enter the file name ==> '))
            func_list = read_in_file(filename)
            file_is_invalid = False
        except FileNotFoundError: print('Could not open file "{}"'.format(filename)) 
    
    month,crimes = get_max_month(create_reported_month_dict(func_list))
    crime,numcrimes = get_max_crimes(create_offense_dict(func_list))

    print('\nThe month with the highest number of crimes is {} with {} offenses'.format(month,crimes))
    print('The offense with the highest number of crimes is "{}" with {} offenses\n'.format(crime,numcrimes))

    zip_code_dict = create_offense_by_zip(func_list)

    running = True
    while running:
        offense = input('Enter an offense ')
        if offense in zip_code_dict.keys():
            print('\n{} offenses by zip code'.format(offense))
            print('{:<10}{:>20}'.format('Zip Code','# Offenses'))
            print('=' * 30)
            for zip,num in zip_code_dict[offense].items():
                print('{:<10}{:>20}'.format(zip,num))
            running = False
        else:
            print('Not a valid offense, please try again')
            running = True