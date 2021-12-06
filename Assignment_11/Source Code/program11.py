########################################################################
##
## CS 101 Lab
## Program 11
## Mason Komer
## maktcr@umsystem.edu
##
## PROBLEM : Make a clock
##
## ALGORITHM : 
##      
## 
## ERROR HANDLING: none
##                  
##
## OTHER COMMENTS:
##  in the example on the assignment, the 12hour clock is not handled correctly ( clock(13,58,59,1) should output 1:58:59 pm, not 13:58:59 pm)
##      
########################################################################
import time

class Clock:
    def __init__(self,hours,mins,secs,type = 0):
        self.hours = hours
        self.minutes = mins
        self.seconds = secs
        self.clock_type = type
    
    def __str__(self):
        if self.clock_type == 0:
            return str(('{:02}:{:02}:{:02}' .format(self.hours,self.minutes,self.seconds)))
        else:
            if self.hours >= 13:
                return str('{}:{:02}:{:02} {}'.format(self.hours - 12,self.minutes,self.seconds,'p.m.'))
            elif self.hours < 13:
                return str('{}:{:02}:{:02} {}' .format(self.hours,self.minutes,self.seconds,'a.m.'))

    def tick(self):
        self.seconds += 1

        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0

            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0

running = True   
while running:
    hours = int(input('What is the current hour ==> '))
    minutes = int(input('What is the current minute ==> '))
    seconds = int(input('What is the current second ==> '))

    clock = Clock(hours,minutes,seconds,1)

    while True:
        print(clock)
        clock.tick()
        time.sleep(1)
