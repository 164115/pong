from tkinter import *

window = Tk()
canvas = Canvas(window, width="1920", height="1080", background="black")
canvas.pack()

can_move_down = True
can_move_up = True


def key_released(event):
    global player_x_val, player_y_vel
    if event.keysym == "Up" or event.keysym == "Down":
        player_y_vel = 0


def key_pressed(event):
    global player_x_val, player_y_vel, can_move_down, can_move_up
    if event.keysym == "Up" and can_move_down:
        player_y_vel = -7
    elif event.keysym == "Down" and can_move_up:
        player_y_vel = 7


def move_stuff():
    global player_y_vel, player_x_val, can_move_down, can_move_up
    canvas.move(player, player_x_val, player_y_vel)
    window.after(16, move_stuff)
    can_move_down = True
    can_move_up = True
    if canvas.coords(player)[1] < 0:  # Top wall
        player_y_vel = 0
        can_move_down = False
    elif canvas.coords(player)[3] > 920:  # Right wall
        player_y_vel = 0
        can_move_up = False




player_x_val = 0
player_y_vel = 0

canvas.bind("<KeyPress>", key_pressed)
canvas.bind("<KeyRelease>", key_released)
canvas.focus_set()
player = canvas.create_rectangle(20, 100, 100, 400, fill="white")

move_stuff()

window.mainloop()