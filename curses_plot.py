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

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if (len(sys.argv)<2):
    print("few args")
    exit()

mul = int(sys.argv[1])
time.sleep(.1)

def main(stdscr):
    curses.curs_set(0)

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("",4353))
    arrSize = 500
    arr = np.array(np.full(arrSize, -1000.0))

    # log file
    with open('log_file.csv', mode='w') as log:
        log_writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        log_writer.writerow(['John Smith', 'Accounting', 'November'])
        log_writer.writerow(['Erica Meyers', 'IT', 'March'])    

# feeder
    ind = arrSize-1
    tt1=tt2=hh1=hh2=0
    while 1:
        ind = ind-1
        if ind< 0:
            ind = arrSize-1 
        #arr[ind] = np.sin((ind/10.0))*mul+50
        #msg, add = sock.recvfrom(1024)
        #lst = msg.decode().split (",")
        #tt = float(lst[2])
        #hh = float(lst[3])
        #if int(lst[1])==73:
        #    tt1 = tt; hh1=hh 
        #else:
        #    tt2 = tt; hh2=hh
        #arr[ind] = np.abs(hh1-hh2)  
        arr[ind] = np.sin((ind/10.0))*(mul) + 500.0
        plot_array.plot(stdscr,arr,ind)
        time.sleep(.1)    
    #stdscr.getkey()
print(12)
time.sleep(0.2)
wrapper(main)
