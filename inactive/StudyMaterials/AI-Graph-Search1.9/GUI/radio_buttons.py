from tkinter import *
from tkinter.ttk import *
from Algorithms.Search_Algorithms import *
from tkinter import messagebox
import importlib
import inspect
# Import the module
module_name = "Algorithms.Search_Algorithms"
module = importlib.import_module(module_name)

# List all classes in the module
classes_in_module = [cls for name, cls in inspect.getmembers(module, inspect.isclass)]
#get rid of the base class
classes_in_module = [cls for cls in classes_in_module if cls.__name__ != "BaseAlgorithm"]
# Print the number of classes imported
class AlgorithmsRadioButtons(Frame):

    def __init__(self,root,submit_callback,canvas=None):
        """
        Buttons for Algorithm Selections 
        """
        Frame.__init__(self, root)
        self.__depth_limited_text = Entry(self)
        self.__algorithms_label = Label(self,text = "Search Algorithms :")
        self.__algorithms_combobox = Combobox(self,state="readonly")
        self.__algorithms_combobox['values'] = [cls.__name__ for cls in classes_in_module]
        self.__algorithms_combobox.set(classes_in_module[0].__name__)
        self.__algorithm_args = {}


        self.__button = Button(self ,text="Start Search" , command=self.__start_search)
        self.__submit_callback =submit_callback
        self.__canvas = canvas
        self.__depth_limited_text.bind('<FocusIn>',lambda x : self.__canvas.undo_selection())
        self.__pack_on_screen()

    def __pack_on_screen(self):
        """
        Button Position Definitions
        """
        self.__algorithms_label.grid(row=0,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__algorithms_combobox.grid(row=1,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__button.grid(row=2,column=0,sticky="S",padx=(0, 5),pady=(5,5))
    
    def add_algorithm(self,algorithm_name,algorithm_number):
        """
        Add Algorithm to the radio buttons
        """
        Radiobutton(self, text=algorithm_name, variable=self.__var, value=algorithm_number).grid(row=algorithm_number+1,column=0,padx=(0, 5),pady=(5,5),sticky="W")

    def get_algorithm(self):
        cls= [cls for cls in classes_in_module if cls.__name__ == self.__algorithms_combobox.get()]
        if cls:
            return cls[0]
        else:
            return None

    def __start_search(self):
        """
        Links button with Search_Algorithms
        """
        cls=self.get_algorithm()
        if cls:
            self.__submit_callback(cls)
        else:
            messagebox.showerror(title="Submit Error",message="You need to choose at least one algorithm")

    def disable(self):
        self.__button.config(state=DISABLED)
    
    def enable(self):
        self.__button.config(state=NORMAL)

class AlgorithmsRadioButtonsStudent(Frame):

    def __init__(self,root,submit_callback=None,canvas=None):
        """
        Buttons for Algorithm Selections 
        """
        Frame.__init__(self, root)
        self.__depth_limited_text = Entry(self)
        self.__algorithms_label = Label(self,text = "Search Algorithms :")
        self.__algorithms_combobox = Combobox(self,state="readonly")
        self.__algorithms_combobox['values'] = [cls.__name__ for cls in classes_in_module]
        self.__algorithms_combobox.set(classes_in_module[0].__name__)

        self.__canvas = canvas
        self.__depth_limited_text.bind('<FocusIn>',lambda x : self.__canvas.undo_selection())
        self.__pack_on_screen()
    def __pack_on_screen(self):
        """
        Button Position Definitions
        """
        self.__algorithms_label.grid(row=0,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__algorithms_combobox.grid(row=1,column=0,sticky="W",padx=(0, 5),pady=(5,5))


    def get_algorithm(self):
        cls= [cls for cls in classes_in_module if cls.__name__ == self.__algorithms_combobox.get()]
        if cls:
            return cls[0]
        
    def disable(self):
        # self.__button.config(state=DISABLED)
        pass
    
    def enable(self):
        # self.__button.config(state=NORMAL)
        pass

if __name__ ==  "__main__":
    
    root = Tk()

    content = AlgorithmsRadioButtons(root)
    content.grid(column=0, row=0, sticky=(N, S, E, W))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)


    root.mainloop()    

