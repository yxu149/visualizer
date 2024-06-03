from tkinter import *
from tkinter.ttk import *
from Algorithms.Search_Algorithms import *
from Algorithms.Custom_Algorithms import *
from tkinter import messagebox
import importlib
import inspect
from .settings import CUSTOM_ALGORITHMS_PATH
import sys
from shutil import copyfile
from tkinter.filedialog import askopenfilename
# Import the module

module_name = "Algorithms.Search_Algorithms"
custom_module_name = "Algorithms.Custom_Algorithms"
module = importlib.import_module(module_name)
custom_module = importlib.import_module(custom_module_name)

# List all classes in the module
classes_in_module = [cls for name, cls in inspect.getmembers(module, inspect.isclass)]
#get rid of the base class
classes_in_module = [cls for cls in classes_in_module if cls.__name__ != "BaseAlgorithm"]
classes_in_module.extend([cls for name, cls in inspect.getmembers(custom_module, inspect.isclass)])
class AlgorithmsRadioButtons(Frame):

    def __init__(self,root,submit_callback,canvas=None):
        """
        Buttons for Algorithm Selections 
        """
        Frame.__init__(self, root)
        self.__algorithms_label = Label(self,text = "Search Algorithms :")
        self.__algorithms_combobox = Combobox(self,state="readonly")
        self.__algorithms_combobox['values'] = [cls.__name__ for cls in classes_in_module]
        self.__algorithms_combobox.set(classes_in_module[0].__name__)
        self.__arg_text = Label(self,text="Optional Arguments:")
        self.__algorithm_args = Entry(self,)
        # self.__algorithm_args.insert(0,"")


        self.__button = Button(self ,text="Start Search" , command=self.__start_search)
        self.__load_button = Button(self ,text="Load algo" , command=self.open_custom_algorithms)
        self.__submit_callback =submit_callback
        self.__canvas = canvas
        self.__pack_on_screen()
    
    def open_custom_algorithms(self):
        
        # open file
        file_path=askopenfilename(defaultextension=".py",filetypes=[("Python files","*.py")])
        if file_path:
            #copy file to custom algorithms
            copyfile(file_path,CUSTOM_ALGORITHMS_PATH)
            #pop up message
            messagebox.showinfo(title="Success",message="Algorithm loaded successfully please restart program")
            #restart
            sys.exit()

    def __pack_on_screen(self):
        """
        Button Position Definitions
        """
        self.__algorithms_label.grid(row=0,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__algorithms_combobox.grid(row=1,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__arg_text.grid(row=2,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__algorithm_args.grid(row=3,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__button.grid(row=4,column=0,sticky="S",padx=(0, 5),pady=(5,5))
        self.__load_button.grid(row=5,column=0,sticky="S",padx=(0, 5),pady=(5,5))
    

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
    
    def get_args(self):
        args=self.__algorithm_args.get()
        if args == "":
            return {}
        #pack to dictionary
        args = dict([arg.split("=") for arg in args.split(",")])
        return args

class AlgorithmsRadioButtonsStudent(Frame):

    def __init__(self,root,submit_callback,canvas=None):
        """
        Buttons for Algorithm Selections 
        """
        Frame.__init__(self, root)
        self.__algorithms_label = Label(self,text = "Search Algorithms :")
        self.__algorithms_combobox = Combobox(self,state="readonly")
        self.__algorithms_combobox['values'] = [cls.__name__ for cls in classes_in_module]
        self.__algorithms_combobox.set(classes_in_module[0].__name__)
        self.__arg_text = Label(self,text="Optional Arguments:")
        self.__algorithm_args = Entry(self,)
        # self.__algorithm_args.insert(0,"")
        self.__pack_on_screen()

    def __pack_on_screen(self):
        """
        Button Position Definitions
        """
        self.__algorithms_label.grid(row=0,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__algorithms_combobox.grid(row=1,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__arg_text.grid(row=2,column=0,sticky="W",padx=(0, 5),pady=(5,5))
        self.__algorithm_args.grid(row=3,column=0,sticky="W",padx=(0, 5),pady=(5,5))

    def get_algorithm(self):
        cls= [cls for cls in classes_in_module if cls.__name__ == self.__algorithms_combobox.get()]
        if cls:
            return cls[0]
        else:
            return None
        
    def disable(self):
        # self.__button.config(state=DISABLED)
        pass
    
    def enable(self):
        # self.__button.config(state=NORMAL)
        pass
    def get_args(self):
        args=self.__algorithm_args.get()
        if args == "":
            return {}
        #pack to dictionary
        args = dict([arg.split("=") for arg in args.split(",")])
        return args

if __name__ ==  "__main__":
    
    root = Tk()

    content = AlgorithmsRadioButtons(root)
    content.grid(column=0, row=0, sticky=(N, S, E, W))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)


    root.mainloop()    

