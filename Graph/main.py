import sys
from gui.parts.main_canvas import *

sys.path.append(BASE_DIR)

from tkinter import *

if __name__ == "__main__": 
    root = Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w = 1290 if w > 1290 else w
    h = 720 if h > 720 else h
    root.geometry("%dx%d+0+0" % (w, h))

    root.title('Visualizer App')
    canvas = MainCanvas(root, 10, 720) 

    canvas.grid(row=0, column=0)

    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    for arg in sys.argv:
        if arg[-5:] == '.gtxt':
          canvas.get_drawing_canvas().load(arg)  

    root.mainloop()