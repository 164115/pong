from tkinter import *
window = Tk()
canvas = Canvas(window, width="1920", height="1080", background="black")
canvas.pack()


class player:
    def __init__(self, c, w):
        self.player_x_val = 0
        self.player_y_vel = 0
        self.can_move_down = True
        self.can_move_up = True
        self.player_object = canvas.create_rectangle(20, 100, 100, 400, fill="white")
        self.canvas = c
        self.window = w

    def key_released(self, event):
        if event.keysym == "Up" or event.keysym == "Down":
            self.player_y_vel = 0

    def key_pressed(self, event):
        if event.keysym == "Up" and self.can_move_down:
            self.player_y_vel = -7
        elif event.keysym == "Down" and self.can_move_up:
            self.player_y_vel = 7

    def move_stuff(self):
        self.canvas.move(player, self.player_x_val, self.player_y_vel)
        self.window.after(16, self.move_stuff)
        self.can_move_down = True
        self.can_move_up = True
        if self.canvas.coords(self.player_object)[1] < 0:  # Top wall
            self.player_y_vel = 0
            self.can_move_down = False
        elif self.canvas.coords(self.player_object)[3] > 920:  # Bottom wall
            self.player_y_vel = 0
            self.can_move_up = False

    def initialise_player(self):
        self.canvas.bind("<KeyPress>", self.key_pressed)
        self.canvas.bind("<KeyRelease>", self.key_released)
        self.canvas.focus_set()
        self.move_stuff()


player_1 = player(canvas, window)
player_1.initialise_player()


window.mainloop()
