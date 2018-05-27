#https://stackoverflow.com/questions/2515244/how-to-scroll-text-in-python-curses-subwindow#2523020

import curses

stdscr = None
bounds = None
topbar = None
window = None

def init():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)

def close():
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

def setup():
    global bounds
    bounds = (stdscr.getmaxyx())
    topbar = curses.newwin(3,bounds[1],0,0)
    window = curses.newwin(bounds[0]-3,bounds[1],3,0)
    topbar.border('|', '|', '_', '_', ' ', ' ', '|', '|')
    topbar.refresh()
    
init()
setup()
    
from time import sleep

sleep(5)

close()

print bounds
