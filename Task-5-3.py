from robot import *

while is_free_right():
    move_right()
    if(is_cell_painted() and is_free_down()):
        move_down()
        paint()
        move_up()