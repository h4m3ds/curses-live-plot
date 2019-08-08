
import curses
import time
import numpy as np

def scrPer(w,val):
    return np.clip(int((w*val/100.0)) , 0, w)

def plot(stdscr,val,ind):
    stdscr.clear()
    curses.init_pair(10,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_RED)
    curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)
    h,scrWidth = stdscr.getmaxyx()
    #text

    #val =np.array( [-1000.0, -1000.0, 0.001,0.001,0.001,-.5, 0.0 , 10.0 ]); ind=len(val)-1; h=100
    arri = np.array(list(range(ind,len(val)))+list(range(0,ind)))
    
    #  IND-2
    #  IND -1
    #  IND 0
    #  IND OLD
    #mean

    valmn=np.array([])
    index = []
    valsum=0.0; ln=0
    mxm=mnm=0

    for i in iter(range(min(len(val),h))): 
        if val[arri[i]]!=-1000: 
            valsum = valsum+val[arri[i]]; ln=ln+1; index.append(i)
    #mn = valsum/ln
    #valmx = .01+max(abs( val[arri[index]] -mn )) 
    
    valmn=[]  
    valrl = []
    for i in iter(range(min(len(val),h))): 
        if val[arri[i]]!=-1000: 
            valmn.append(  val[arri[i]] )   # value scaled min - max => 0 -
            valrl.append(  val[arri[i]] )
        else:
            valmn.append(-1000)
    
    mnm = min(valrl)-0.001
    mxm = max(valrl)+0.001
    mid = np.mean([mnm,mxm])

    stdscr.addstr(0,0,"{} ".format(round(mnm,2)), curses.color_pair(10) ) #
    stdscr.addstr(0,round(scrWidth/2),"{}".format(round(val[ind],2)))
    stdscr.addstr(0,scrWidth-5,"{}".format(round( mxm,2)), curses.color_pair(10))
    #stdscr.addstr(1,0," {}".format(mn)) #scrPer(w,val[arri[0]])
    for i in iter(range(min(len(val),h-1))): #range(len(val))
        if val[arri[i]]!=-1000:
            pos = scrPer(scrWidth, (valmn[i]-mnm) * (100.0/(mxm-mnm)) )
            if pos>=scrWidth:
                pos=scrWidth-1
            if pos<0:
                pos=0
            try:
                stdscr.addch(i,pos,'0', curses.color_pair(1)) 
            except:
                print(pos)
                print(scrWidth)
                time.sleep(2)
            
    stdscr.refresh()
