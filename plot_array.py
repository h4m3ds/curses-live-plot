

import curses
import time
import numpy as np

def scrPer(w,val):
    return np.clip(int((w*val/100.0)) , 0, w)

def plot(stdscr,val,ind):
    stdscr.clear()
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    h,w = stdscr.getmaxyx()
    #text

    #val =np.array( [-1000, .002]); ind=len(val); h=100
    
    arri = np.array(list(range(ind,len(val)))+list(range(0,ind)))
    
    #mean
    valmn=np.array([])
    index = []
    valsum=0.0; ln=0
    for i in iter(range(min(len(val),h))): 
        if val[arri[i]]!=-1000: 
            valsum = valsum+val[arri[i]]; ln=ln+1; index.append(i)
    mn = valsum/ln
    valmx = .01+max(abs( val[arri[index]] -mn )) 
    
    valmn=[]
    for i in iter(range(min(len(val),h))): 
        if val[arri[i]]!=-1000: 
            valmn.append( (val[arri[i]]-mn) *50.0/valmx + 50 )
        else: 
            valmn.append(-1000)
    
     

    stdscr.addstr(0,0," {}".format(round(valmn[0],2))) #scrPer(w,val[arri[0]])
    stdscr.addstr(1,0," {}".format(mn)) #scrPer(w,val[arri[0]])
    for i in iter(range(min(len(val),h))): #range(len(val))
        if val[arri[i]]!=-1000:
            pos = scrPer(w,valmn[i])
            if pos>=w:
                pos=w-1
            if pos<0:
                pos=0
            try:
                stdscr.addch(i,pos,'o') 
            except:
                print(pos)   
                print(w)
                time.sleep(2)        
            
    stdscr.refresh()
