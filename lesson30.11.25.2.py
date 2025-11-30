import tkinter

'''def move_by_keys(event):
    if event.keysym == 'Up':
        canvas.move(oval, 0, -20)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 20)
    elif event.keysym == 'Left':
        canvas.move(oval, -20, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 20, 0)

win = tkinter.Tk()
label = tkinter.Label(win, text='INGINIRIUM')
label.pack()
canvas = tkinter.Canvas(win, bg='#fff', width=700, height=700)
oval = canvas.create_oval((300, 300), (400, 400), fill='yellow')
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()'''


win = tkinter.Tk()
canvas = tkinter.Canvas(win, bg='white', width=400, height=400)
a = 800
y = 20
x = 20
c = 0
for i in range(8):
    y += 20
    x += 20
    canvas.create_line((0, y), (a, y), fill='black')
    canvas.create_line((x, 0), (x, a), fill='black')
canvas.pack()
win.mainloop()