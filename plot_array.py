
import curses
import time
import numpy as np

def scrPer(w,val):
    return int(round(w*val/100.0,2))
def plot(stdscr,val,ind):
    stdscr.clear()
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    h,w = stdscr.getmaxyx()
    #text

    val = [np.nan, 100.1, 200.2, 300.3]
    
    arri = list(range(ind,len(val)))+list(range(0,ind-1))
    valdiff =   val-np.nanmean(val) 
    valmx = np.nanmax(abs(valdiff))/50.0
    valmn =  50 + valdiff /valmx 
    if ~np.isnan(val[arri[0]]):
        stdscr.addstr(0,scrPer(w,valmn[arri[0]])," {}".format(round(val[arri[0]],2)))
    
    for i in iter(range(min(len(val),h))): #range(len(val))
        if ~np.isnan(val[arri[i]]):
            pos = scrPer(w,valmn[arri[i]])
            if pos>=w:
                pos=w-1
            if pos<0:
                pos=0
            stdscr.addch(i,pos,'o')            
    stdscr.refresh()
