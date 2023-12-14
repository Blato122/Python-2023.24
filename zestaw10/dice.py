import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # sudo apt install python3-pil.imagetk
import random
import os

W, H = 500, 500

def roll():
    n = random.randint(1, 6)
    image = Image.open(os.path.join(os.getcwd(), image_names[n-1]))
    image = image.resize((W, H), Image.ANTIALIAS)
    resized_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=resized_image)
    canvas.image = resized_image

main = tk.Tk()
main.title("Dice")
main.geometry(str(W) + "x" + str(H))

image_names = [name for name in os.listdir(os.getcwd()) if name != os.path.basename(__file__)]

canvas = tk.Canvas(main, width=W, height=H)
canvas.grid(row=1, column=0)

button = ttk.Button(main, text="Click to roll the dice", command=roll)
button.grid(row=0, column=0)

main.mainloop()