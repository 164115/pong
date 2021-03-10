from tkinter import *
window = Tk()
canvas = Canvas(window, width="1920", height="1080", background="black")
canvas.pack()


class player:
    def __init__(self, c, ):
        self.player_x_val = 0
        self.player_y_val = 0
        self.can_move_down = True
        self.can_move_up = True
        self.player_object = canvas.create_rectangle(20, 100, 100, 400, fill="white")
        self.canvas = c

    def key_released(self, event):
        if event.keysym == "Up" or event.keysym == "Down":
            self.player_y_val = 0

    def key_pressed(self, event):
        if event.keysym == "Up" and self.can_move_down:
            self.player_y_val = -7
        elif event.keysym == "Down" and self.can_move_up:
            self.player_y_val = 7

    def move_player(self):
        self.canvas.move(self.player_object, self.player_x_val, self.player_y_val)
        self.can_move_down = True
        self.can_move_up = True
        if self.canvas.coords(self.player_object)[1] < 0:  # Top wall
            self.player_y_val = 0
            self.can_move_down = False
        elif self.canvas.coords(self.player_object)[3] > 920:  # Bottom wall
            self.player_y_val = 0
            self.can_move_up = False

    def initialise_player(self):
        self.canvas.bind("<KeyPress>", self.key_pressed)
        self.canvas.bind("<KeyRelease>", self.key_released)
        self.canvas.focus_set()
        self.move_player()


"""---------------------------------- yao code ----------------------------------"""


def move_ball():
    global ball_x_val, ball_y_val
    if running == 1:
        canvas.move(ball, ball_x_val, ball_y_val)
        # Bounce off walls
        if canvas.coords(ball)[2] > 1920:  # right wall
            ball_x_val = -ball_x_val


ball_x = 800
ball_y = 800
target_x = ball_x
target_y = ball_y
ball_width = 100
ball_height = 100
ball_x_val = 0
ball_y_val = 20
running = 1

canvas.bind("<Button-2", )
canvas.focus_set()
ball = canvas.create_rectangle(ball_x, ball_y, ball_x + ball_width, ball_y + ball_height, fill="blue")



def stop():
    global running
    if running == 1:
        running = 0
    elif running == 0:
        running = 1


stop_button = Button(window, command=stop, text="Stop bouncing!")
stop_button.pack()

exit_button = Button(window, command=window.destroy, text="Kill.")
exit_button.pack()

"""---------------------------------- yao code ----------------------------------"""

player_1 = player(canvas)
player_1.initialise_player()

while True:
    canvas.after(16)
    player_1.move_player()
    move_ball()
    canvas.update()
