import tkinter as tk

W, H, = 600, 500
x, y, = W // 2 , H // 2
vx, vy = 10, -10
BALL_Radius = 20
TIMEOUT = 25

x1 = W // 2
PLATFORM_H = 50
PLATFORM_W = 250
points = 0
game_mode = True
root = tk.Tk()

canvas = tk.Canvas(root, width=W, height=H,)
canvas.pack()

ball = canvas.create_oval(x - BALL_Radius, y - BALL_Radius, x + BALL_Radius, y + BALL_Radius, fill = 'yellow')
platform = canvas.create_rectangle(x1 - PLATFORM_W // 2, H, x1 + PLATFORM_W // 2, H - PLATFORM_H, fill = 'yellowgreen')
score = canvas.create_text(W - 60, 60, text='0', font=('Times New Roman', 35))

def game():
    global x, y, vx, vy, points, game_mode
    x, y = x + vx, y + vy
    canvas.coords(ball, x - BALL_Radius, y - BALL_Radius, x + BALL_Radius, y + BALL_Radius)
    if y <= BALL_Radius:
        vy = -vy
    if x <= BALL_Radius or x >= W - BALL_Radius:
        vx = -vx
    if x1 - PLATFORM_W // 2 <= x <= x1 + PLATFORM_W // 2 and y == H - (BALL_Radius + PLATFORM_H):
        vy = -vy
        points += 1
        canvas.itemconfig(score, text=str(points))
    root.update()
    if y < (H - BALL_Radius):
        root.after(TIMEOUT, game)
    else:
        canvas.create_text(W // 2, H // 2, text='GAME OVER', fill='red', font=('Times New Roman', 60))
        game_mode = False

def keyboard(event):
    global x1
    if event.keycode == 37:
        x1 -= 50
    if event.keycode == 39:
        x1 += 50
    if game_mode:
        canvas.coords(platform, x1 - PLATFORM_W // 2, H, x1 + PLATFORM_W // 2, H - PLATFORM_H)


def mouse_move(event):
    global x1
    x1 = event.x
    if game_mode:
        canvas.coords(platform, x1 - PLATFORM_W // 2, H, x1 + PLATFORM_W // 2, H - PLATFORM_H)



game()
root.bind('<Key>', keyboard)
canvas.bind('<Motion>', mouse_move)
root.mainloop()