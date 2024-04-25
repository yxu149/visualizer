import tkinter as tk
from settings.settings import *

# call Button to have a button made
@staticmethod
def create_button(parent, img_path, callback): 
    img = tk.PhotoImage(file=img_path)
    button = tk.Button(parent, image=img, command=callback, bg=BUTTON_BG)
    button.image = img 
    print("Made button", button, "with image from", img_path)
    return button 
