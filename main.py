import tkinter as tk
import random
from tkinter import ttk
import numpy as np
from numpy import cos,sin,tan,arcsin,arccos,arctan,log,e

root = tk.Tk()

class Block:
    def __init__(self, root):
        # Create parts of GUI
        self.f_function = tk.Frame(root)
        self.f_border = tk.Frame(root)
        self.f_dots = tk.Frame(root)
        self.function_text = tk.Label(self.f_function, text="Write down the function", width="40")
        self.border_text = tk.Label(self.f_border, text="Write start and end points", width="20")
        self.dots_text = tk.Label(self.f_dots, text="Write quantity of dots", width="20")
        self.function = tk.Entry(self.f_function, width="40")
        self.start_point = tk.Entry(self.f_border, width="10")
        self.end_point = tk.Entry(self.f_border, width="10")
        self.dots = tk.Entry(self.f_dots, width="10")
        self.result = tk.Label(root, width="40")
        self.start = tk.Button(root, text="Start", command=self.approximate, width="10")
        self.progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL,
                                            length=300, mode='determinate')
        #self.plot = tk.Canvas(width=500, height=300, bg="white")

        self.f_function.pack()

        self.result.pack(side=tk.BOTTOM, pady=10)
        #self.plot.focus_set()
        #self.plot.pack(side=tk.BOTTOM)
        self.progress_bar.pack(side=tk.BOTTOM, pady=10)
        self.start.pack(side=tk.BOTTOM)
        self.f_border.pack(side=tk.RIGHT)
        self.f_dots.pack(side=tk.RIGHT)
        self.function_text.pack()
        self.function.pack()
        self.border_text.pack()
        self.start_point.pack()
        self.end_point.pack(side=tk.BOTTOM)
        self.dots_text.pack()
        self.dots.pack()

    def approximate(self):
        # Change double ^ to **
        function = self.function.get().replace("^", "**")
        # Declare variable
        dots_negative = 0
        dots_positive = 0
        maximum = -10 ** 11
        minimum = 10 ** 11
        # Get variable from entries
        dots = int(self.dots.get())
        a = int(self.start_point.get())
        b = int(self.end_point.get())

        for x in np.arange(a, b + 1, 0.0001):
            y = eval(function)
            if y >= maximum:
                maximum = y
            if y <= minimum:
                minimum = y

        if minimum <= 0 and maximum <= 0:
            maximum = 0
        elif minimum > 0 and maximum > 0:
            minimum = 0

        area = (maximum - minimum) * (b - a)

        for progress in range(1, dots):
            # Progress bar
            self.progress_bar["value"] = dots * 100 / progress

            x = random.uniform(a, b)
            y = random.uniform(minimum, maximum)

            f_y = eval(function)
            if 0 < y <= f_y:
                dots_positive += 1
            elif f_y <= y < 0:
                dots_negative += 1

        self.result["text"] = str(round(((dots_positive - dots_negative) / dots) * area, 6))


first_block = Block(root)
root.mainloop()
