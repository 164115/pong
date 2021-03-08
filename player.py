from tkinter import *
import random

window = Tk()
canvas = Canvas(window, width="1920", height="1080", background="blanchedalmond")
canvas.pack()


def key_released(event):
    global player_x_val, player_y_vel
    if event.keysym == "Up" or event.keysym == "Down":
        player_y_vel = 0


def key_pressed(event):
    global player_x_val, player_y_vel
    print("event", event)
    if event.keysym == "Up":
        player_y_vel = -7
    if event.keysym == "Down":
        player_y_vel = 7


def move_stuff():
    canvas.move(walter, player_x_val, player_y_vel)
    window.after(16, move_stuff)

"""
def barrier(event):
    global player_x_val, player_y_vel
    if canvas.coords(walter)[2] == 1920:  # Bottom wall
        if event.keysym == "Down":
            player_y_vel = 7

    if canvas.coords(walter)[1] == 0:  # Top wall
        if event.keysym == "Up":
            player_y_vel = -14
"""


player_x_val = 0
player_y_vel = 0

canvas.bind("<KeyPress>", key_pressed)
canvas.bind("<KeyRelease>", key_released)
canvas.focus_set()
walter = canvas.create_rectangle(20, 100, 100, 400, fill="white")

move_stuff()

window.mainloop()