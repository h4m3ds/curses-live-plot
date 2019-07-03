#!/usr/bin/python
from curses import wrapper
import curses
import time
import numpy as np
import csv
import math 
import sys
import numpy

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

# input comma separated elements as string 
str = str (input ("Enter comma separated integers: "))
print ("Input string: ", str)
# conver to the list
list = str.split (",")
print ("list: ", list)
# convert each element as integers
li = []
for i in list:
	li.append(float(i))
# print list as integers
print ("list (li) : ", li)


if (len(sys.argv)<2):
    print("few args")
    exit()

mul = int(sys.argv[1])
time.sleep(1)
def draw_array(stdscr,val,ind):
    stdscr.clear()
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    h,w = stdscr.getmaxyx()
    
    #text
    stdscr.addstr(0,0,"values in percentage {} from {}".format(ind,len(val)))
    arri = list(range(ind,len(val)))+list(range(0,ind-1))
    for i in iter(range(min(len(val),h))): #range(len(val))
        pos = int((w*val[arri[i]]/100)-1)
        if pos>=w: 
            pos=w-1
        if pos<0 : 
            pos=0
        
        stdscr.addch(i,pos,'#')
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    
    with open('log_file.csv', mode='w') as log:
        log_writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        log_writer.writerow(['John Smith', 'Accounting', 'November'])
        log_writer.writerow(['Erica Meyers', 'IT', 'March'])    

    # feeder
    arr = np.zeros(1000)
    for ind in list(np.arange(len(arr)-1,0,-1)):
        arr[ind] = np.sin((ind/10.0))*mul+50
        draw_array(stdscr,arr,ind)
        time.sleep(.1)    
    #stdscr.getkey()

print(12)
time.sleep(0.2)
wrapper(main)
