
#!/usr/bin/python
from curses import wrapper
import curses
import time
import numpy as np
import csv
import math 
import sys
import socket
import plot_array
import datetime
from time import strftime


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if (len(sys.argv)<2):
    print("few args")
    exit()

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

time.sleep(.1)

def main(stdscr):
    curses.curs_set(0)
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("",4353))
    arrSize =1000
    arr = np.array(np.full(arrSize, -1000.0))


   
# feeder
    ind = arrSize-1
    tt1=tt2=hh1=hh2=pp1=pp2=0
    while 1:
        h,scrWidth = stdscr.getmaxyx()
        ind = ind-1
        if ind< 0:
            ind = arrSize-1
        if(1): # socket 
            msg, add = sock.recvfrom(1024)
            lst = msg.decode().split (",")
            tt = float(lst[2])
            hh = float(lst[3])
            pp = float(lst[4])
            if int(lst[1])==20:
                tt1 = tt; hh1=hh; pp1=pp 
            else:
                tt2 = tt; hh2=hh; pp2=pp
            
            if arg2==0:
                arr[ind] = (hh1-hh2)
            elif arg2==1:
                arr[ind] = (tt1-tt2)
            else:
                arr[ind] = (pp1-pp2)
        else:
            arr[ind] = np.sin((ind/10.0))*(arg1*ind) + 0
        
        
        plot_array.plot(stdscr,arr,ind)
        stdscr.addstr(3,0,"Humd: {} per".format(round(hh1,2)), curses.color_pair(1)); stdscr.addstr(3,scrWidth-15,"Humd: {} per".format(round(hh2,2)), curses.color_pair(1))
        stdscr.addstr(4,0,"Temp: {} deg".format(round(tt1,2)), curses.color_pair(2)); stdscr.addstr(4,scrWidth-15,"Temp: {} deg".format(round(tt2,2)), curses.color_pair(2))
        stdscr.addstr(5,0,"Pres: {} hpa".format(round(pp1,2)), curses.color_pair(3)); stdscr.addstr(5,scrWidth-15,"Pres: {} hpa".format(round(pp2,2)), curses.color_pair(3))
        
        #log
            # log file
        with open('log_file.csv', mode='a') as log:
            log_writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow([(strftime(strftime("%y_%m_%d_%H_%M_%S"))),hh1,hh2,tt1,tt2,pp1,pp2]) 
         
        stdscr.refresh()
        time.sleep(arg2/10)
    #stdscr.getkey()
print(12)
print(12)

wrapper(main)
