import tkinter as tk
import settings.settings as settings
import gui.utils.hovertext as hovertext 

# call Button to have a button made
@staticmethod
def create_button(parent, img_path, callback, tip=None): 
    img = tk.PhotoImage(file=img_path)
    button = tk.Button(parent, image=img, command=callback, bg=settings.BUTTON_BG)
    button.image = img 
    print("Made button", button, "with image from", img_path)
    hovertext.create_tool_tip(button, text=tip)
    print("Button assigned tip:", tip)
    return button 
