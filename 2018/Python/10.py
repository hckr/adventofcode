#!/usr/bin/env python3
import sys
import re
import tkinter as tk

points = list((tuple(map(int, re.findall(r'-?\d+', line))) for line in sys.stdin))


class Application(tk.Frame):
    def __init__(self, master=None, width=500, height=500, auto_pause=None):
        tk.Frame.__init__(self, master)
        self.master.title('10')
        self.master.geometry(f'{width}x{height}')
        self.width = width
        self.height = height
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.bind("<Configure>", self.on_resize)
        self.bind_all('<Key>', self.on_key)
        self.counter = 0
        self.resolution = 100
        self.delay = 1
        self.pause = False
        self.auto_pause = auto_pause
        self.step = False
        self.direction = 1
        self.update()

    def on_resize(self, event):
        self.width = event.width
        self.height = event.height

    def on_key(self, event):
        if event.char == ' ':
            if self.pause:
                self.resolution = 100
            else:
                self.resolution = 1
            self.pause = not self.pause
        elif event.char == 's':
            self.step = True
            self.direction = 1
        elif event.char == 'a':
            self.step = True
            self.direction = -1

    def update(self):
        global points
        if not self.pause or self.step:
            self.counter += self.direction
            if self.counter == self.auto_pause:
                self.pause = True
            points = [(x + vx * self.direction, y + vy * self.direction, vx, vy)
                      for (x, y, vx, vy) in points]
            self.step = False
        if self.counter % self.resolution == 0 or self.pause:
            min_x = min(points, key=lambda x: x[0])[0]
            min_y = min(points, key=lambda x: x[1])[1]
            max_x = max(points, key=lambda x: x[0])[0]
            max_y = max(points, key=lambda x: x[1])[1]
            self.canvas.delete('all')
            self.canvas.create_text(70, 15, fill='#33aaff', font='monospace 12',
                                    text=f'counter: {self.counter}')
            for p in points:
                x = ((p[0] - min_x) / (max_x - min_x)) * 0.9 * self.width + 0.05 * self.width
                y = ((p[1] - min_y) / (max_y - min_y)) * 0.9 * self.height + 0.05 * self.height
                self.canvas.create_oval(x, y, x, y, width=3, fill='black')
        self.after(self.delay, self.update)


root = tk.Tk()
app = Application(master=root, width=500, height=100, auto_pause=10459)
root.mainloop()
