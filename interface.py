import curses, traceback
if __name__=='__main__': # for initializing the module
    try:
        stdscr=curses.initscr()
        curses.noecho()
        curses.cbreak()
    except:
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exec()  # prints exception

def main(stdscr): # options for screen interface
    global screen
    screen=stdscr.subwin(23,79,0,0)
    screen.box()
    screen.hline(2,1,curses.ACS_HLINE,77)
    screen.refresh()

    # for defining the menu
    file_menu=('File', 'file_func()')
    help_menu=('Help','help_func()')
    exit_menu=('Exit','EXIT')
    
    # for creating the topbar menu
    tb=((file_menu,help_menu,exit_menu))
    while topbar_key_handler():  # topbar menu loop
        draw_dict()

def file_func(): # for user input
    s=curses.newwin(5,102,1)
    s.box()     # the strings below add text in a specified pos
    s.addstr(1,2,'I',hotkey_attr)
    s.addstr(1,3,'nput',menu_attr)
    s.addstr(2,2,'O',hotkey_attr)
    s.addstr(2,3,'utput',menu_attr)
    s.addstr(3,2,'T',hotkey_attr)
    s.addstr(3,3,'type',menu_attr)
    s.addstr(1,2,"  ",hotkey_attr)
    s.refresh()
    c=s.getch() # gets the user's selection
    if c in (ord('I'),ord('i'),curses.KEY_ENTER,10):    # variables listed can activate the menu; MUST use function ord() to perform comparisons to a char value
        curses.echo()
        s.erase
        screen.addstr(5,33,'    '*43,curses.A_UNDERLINE)
        cfg_dict['source']=screen.getstr(5,33)
        curses.noecho()
    else:
        curses.beep()
        s.erase()
    return CONTINUE
    
