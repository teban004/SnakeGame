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

food = [round(sh/2), round(sw/2)]  #set the initial food place
w.addch(food[0], food[1], curses.ACS_PI)  # add the food to the screen

key = curses.KEY_RIGHT  # set initial direction of the snake

# infinite loop for every movement of the snake
while True:
    next_key = w.getch()  # check what the next key is
    key = key if next_key == -1 else next_key  # update the key value only when there is a new key

    # check if the user has lost the game
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]  # determine what the new head of the snake will be

    # determine what key was down
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # insert the new head of the snake
    snake.insert(0, new_head)

    # check if the snake found food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(round(food[0]), round(food[1]), curses.ACS_PI)  # add the food
    else:
        tail = snake.pop()
        w.addch(round(tail[0]), round(tail[1]), ' ')
    
    w.addch(round(snake[0][0]), round(snake[0][1]), curses.ACS_CKBOARD)

