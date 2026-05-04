import cv2 as c
import tkinter as tk
import pygame as pg
import threading as th

def start_pygame():
    pg.init()
    video = c.VideoCapture('video.mp4')
    fps = video.get(c.CAP_PROP_FPS)
    window = pg.display.set_mode((500, 500))
    clock = pg.time.Clock()

    run = True
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        succes, video_image = video.read()
        if succes:
            video_surf = pg.image.frombuffer(
                video_image.tobytes(),
                video_image.shape[1::-1],
                'BGR'
            )
            video_surf = pg.transform.scale(video_surf, (500, 500))
            window.blit(video_surf, (0, 0))
            pg.display.flip()

    pg.quit()
def run_pygame_thread():
    pg_th = th.Thread(target=start_pygame)
    pg_th.start()

root = tk.Tk()
root.title('Pygame and Tkinter')
root.geometry('300x200')

start_button = tk.Button(root, text='start pygame', command=run_pygame_thread)
start_button.pack(pady=10)
exit_button = tk.Button(root, text='end', command=lambda: (pg.quit(), root.quit()))
exit_button.pack(pady=10)

root.mainloop()
