import tkinter

print('start')
win = tkinter.Tk()
win.title('rrrrr')
canvas = tkinter.Canvas(win, bg='#cda4de', width=900, height=900)
canvas.create_oval((300, 300), (500, 600), fill='#87CEFA')
canvas.create_line((0, 0), (100, 200), (300, 300), (200, 100), (0, 0), fill='black')
canvas.pack()
win.mainloop()
print('stop')

