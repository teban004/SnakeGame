import random
import curses

s = curses.initscr()  # initializes the screen
curses.curs_set(0)  # set the cursor to 0 so it doesn't show up in the screen
sh, sw = s.getmaxyx()  # get the width and heigth
w = curses.newwin(sh, sw, 0, 0)  # create a new window and set it to the top left corner
w.keypad(1)  # set keypad input
w.timeout(100)  # set refresh window every 100ms

snk_x = sw/4  # set the initial snake X position
snk_y = sh/2  # set the initial snake Y position

#create initial snake body parts
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]  #set the initial food place
w.addch(food[0], food[1], curses.ACS_PI)  # add the food to the screen

key = curses.KEY_RIGHT  # set initial direction of the snake




