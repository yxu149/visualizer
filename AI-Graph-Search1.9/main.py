import sys
from GUI.settings import * 

sys.path.append(BASE_DIR)

from tkinter import *
from GUI.settings import * 
from tkinter.ttk import *
from GUI.treecanvas import TreeCanvas
from GUI.canvas import DrawingCanvas
from GUI.canvas_student import DrawingCanvasStudent
from GUI.Buttons import *
from GUI.treenode import TreeNode
from GUI.radio_buttons import AlgorithmsRadioButtons,AlgorithmsRadioButtonsStudent
from GUI.Node import Line,Node
from GUI.utils import mouse
from tkinter.filedialog import *
from tkinter import messagebox

import importlib

class MainCanvas(Frame):
    """
    Parameters: Frame - Ttk Frame widget is a container, used to group other widgets together. 

    Main GUI definitions. 
    """
    def __init__(self,root,width=200,height=200):
        self.width = width
        Frame.__init__(self, root,width=width,height=height) 
        mouse.set_root(self)
        self.__drawing_canvas_student = DrawingCanvasStudent(self,event_root = root)
        self.__drawing_canvas = DrawingCanvas(self,event_root = root,
                                              onselect=self.__on_element_selection,onrelease=self.__on_element_release,
                                              student_canvas=self.__drawing_canvas_student)
        
        self.__tree_canvas = TreeCanvas(self)
        self.__tree_canvas_student=TreeCanvas(self)
        self.__control_bar = Button_Bar(self)
        self.__buttons = InteractionButtons(self,self.pause_callback,self.resume_callback,self.terminate_callback,self.delete_all)
        self.__goal_label = Label(self,text = "Goal path :")
        self.__T = Entry(self)
        self.__T.insert(END, "Goal path will appear here")
        self.__T.config(state=DISABLED)

        self.__buttons_student=InteractionButtons(self,self.pause_callback_student,self.resume_callback_student,
                                                  self.terminate_callback_student,self.delete_all_student)
        self.__goal_label_student = Label(self,text = "Goal path :")
        self.__T_student= Entry(self)
        self.__T_student.insert(END, "Goal path will appear here")
        self.__T_student.config(state=DISABLED)

        self.__H_label = Label(self,text = "Weight or Heurastic : ")
        self.__H_text = Entry(self)
        self.__H_text.insert(END, "weight (Line) , Heurastic(Node)")
        self.__H_text.config(state=DISABLED)
        self.__Name_label = Label(self,text = "Change Node Name :")
        self.__Name_text = Entry(self)
        self.__Name_text.insert(END, "Change node name")
        self.__Name_text.config(state=DISABLED)
        self.__Name_text.bind('<Return>',lambda x: self.__change_node())
        self.__H_text.bind('<Return>',lambda x: self.__change_node())
        self.__submit_changes = Button(self ,text="Submit Changes" , command=self.__change_node)
        self.__submit_changes.config(state=DISABLED)
        self.__current_thread = None   
        self.__current_thread_student = None
        self.__radio_buttons = AlgorithmsRadioButtons(self,self.__submit_callback,self.__drawing_canvas)
        self.__radio_buttons_student=AlgorithmsRadioButtonsStudent(self,self.__submit_callback,self.__drawing_canvas_student)
        self.__drawing_canvas_buttons = DrawingCanvasButtons(self,self.__drawing_canvas.delete_all,self.__on_save,self.__on_upload)
        self.__initial_node = None

        
        self.__main_thread_finished = False
        self.__student_thread_finished = False

        self.__testButton=Button(self,text="Test",command=self.test_load)
        # self.main__args = Entry(self)
        # self.student__args = Entry(self)
        root.bind('<Control-s>',lambda x: self.__on_save())
        root.bind('<Control-o>',lambda x: self.__on_upload())
        self.__pack_on_screen()
    def test_load(self):
        module_name = 'Algorithms.custom_algorithms'

        


    
    def __on_save(self):
        """
        Define: the save button
        Call: system - [save as] window

        Saves file to file_path by calling self.__drawing_canvas.save(file_path)
        """
        file_path = asksaveasfilename(initialfile='Untitled.gtxt',
                                        defaultextension=".gtxt",
                                        filetypes=[
                                            ("Graph Documents","*.gtxt")])
        if file_path:
            try:
                self.__drawing_canvas.save(file_path)
            except:
                self.__drawing_canvas.delete_all()
                
    def __on_upload(self):
        """
        Define: the load button
        Call: system - [load saved] window

        Loads file from file_path by calling self.__drawing_canvas.load(file_path)
        """
        file_path = askopenfilename(defaultextension=".gtxt",
                                      filetypes=[
                                        ("Graph Documents","*.gtxt")])
        self.__drawing_canvas.load(file_path)
        # if file_path:
        #     try:
        #         self.__drawing_canvas.load(file_path)
        #     except:
        #         messagebox.showerror(title="File open error",message="Unable to open corrupted file")
        #         self.__drawing_canvas.delete_all()


    def get_drawing_canvas(self):
        """
        Access function. Returns self.__drawing_canvas. 
        """
        return self.__drawing_canvas

    def __on_element_selection(self):
        self.focus()
        if isinstance(self.__drawing_canvas.selected , Line):
            self.__H_text.config(state=NORMAL)
            self.__submit_changes.config(state=NORMAL)
            self.__H_text.delete(0, 'end')
            self.__H_text.insert(END, str(self.__drawing_canvas.selected.get_weight()))
        if isinstance(self.__drawing_canvas.selected , Node):
            self.__Name_text.config(state=NORMAL)
            self.__H_text.config(state=NORMAL)
            self.__submit_changes.config(state=NORMAL)
            self.__H_text.delete(0, 'end')
            self.__Name_text.delete(0, 'end')
            self.__H_text.insert(END, str(self.__drawing_canvas.selected.get_heurastic()))
            self.__Name_text.insert(END, str(self.__drawing_canvas.selected.get_label()))
            
    
    def __on_element_release(self):
        self.__H_text.delete(0, 'end')
        self.__Name_text.delete(0, 'end')
        self.__Name_text.insert(END, "Change node name")
        self.__H_text.insert(END, "weight (Line) , Heurastic(Node)")
        self.__H_text.config(state=DISABLED)
        self.__submit_changes.config(state=DISABLED)
        self.__Name_text.config(state=DISABLED)
        

    def __change_node(self):
        if isinstance(self.__drawing_canvas.selected , Line):
            try:
                self.__drawing_canvas.selected.set_weight(int(self.__H_text.get()))
                self.__drawing_canvas.copy_canvas()
            except :
                messagebox.showerror(title="ValueError",message="Weight value must be an integer")
        elif isinstance(self.__drawing_canvas.selected , Node):
            try:
                self.__drawing_canvas.selected.set_heurastic(int(self.__H_text.get()))
                self.__drawing_canvas.selected.set_label(self.__Name_text.get())
                self.__drawing_canvas.copy_canvas()
            except:
                messagebox.showerror(title="ValueError",message="Heurastic value must be an integer")

    def __submit_callback(self,main_thread_class,**kwargs):
        """
        """
        main_args=self.__radio_buttons.get_args()
        student_args=self.__radio_buttons_student.get_args()
        if self.__drawing_canvas.initial_node and not self.__current_thread:
            
            self.__initial_node = TreeNode(self.__tree_canvas.canvas,0,None,0,self.__tree_canvas.canvas.winfo_width(),self.__drawing_canvas.initial_node)
            self.__current_thread = main_thread_class(self.__initial_node,self.__goal_set,
                                                      self.__goal_notfound,canvas=self.__drawing_canvas, **main_args)
            self.__current_thread.start()

            student_thread_class = self.__radio_buttons_student.get_algorithm()

            self.__initial_node_student=TreeNode(self.__tree_canvas_student.canvas,0,None,0,
                                                 self.__tree_canvas_student.canvas.winfo_width(),self.__drawing_canvas_student.initial_node)
            self.__current_thread_student = student_thread_class(self.__initial_node_student,self.__goal_set_student,
                                                                 self.__goal_notfound_student, canvas=self.__drawing_canvas_student,**student_args)
            self.__current_thread_student.start()

            self.__buttons.delete.config(state=DISABLED)
            self.__buttons.pause.config(state=NORMAL)
            self.__buttons.terminate.config(state=NORMAL)

            self.__buttons_student.delete.config(state=DISABLED)
            self.__buttons_student.pause.config(state=NORMAL)
            self.__buttons_student.terminate.config(state=NORMAL)
            
            self.__control_bar.disable()
            self.__radio_buttons.disable()
            self.__drawing_canvas_buttons.disable()
        elif not self.__drawing_canvas.initial_node:
            messagebox.showerror(title="InitialNode Error",message="Any Graph must contain one initial node")

    def __pack_on_screen(self):
        """
        
        """
        self.__goal_label.grid(row=0,column=1,sticky = "NSEW",padx=(0, 5))
        self.__T.grid(row=1,column=1,sticky = "NSEW",padx=(0, 5))
        self.__Name_label.grid(row=0,column=2,sticky = "NSEW",padx=(0, 5))
        self.__Name_text.grid(row=1,column=2,sticky = "NSEW",padx=(0, 5))
        self.__H_label.grid(row=0,column=3,sticky = "NSEW")
        self.__H_text.grid(row=1,column=3,sticky = "NSEW")
        self.__submit_changes.grid(row=1,column=4,sticky = "NSEW",padx=(5, 0))
        self.__tree_canvas.grid(row=2,column=1,sticky = "NSEW")
        self.__drawing_canvas.grid(row=2,column=2,columnspan=2,sticky = "NSEW")
        self.__control_bar.grid(row=2,column=4,sticky = "NSEW")
        self.__buttons.grid(row=3,column=1)
        self.__drawing_canvas_buttons.grid(row=3,column=2,columnspan=2)
        self.__radio_buttons.grid(row=0,column=0,rowspan=4,sticky="NSEW")


        self.__drawing_canvas_student.grid(row=2,column=5,sticky = "NSEW")
        self.__goal_label_student.grid(row=0,column=6,sticky = "NSEW",padx=(0, 5))
        self.__T_student.grid(row=1,column=6,sticky = "NSEW",padx=(0, 5))
        self.__tree_canvas_student.grid(row=2,column=6,sticky = "NSEW") 
        self.__radio_buttons_student.grid(row=0,column=7,rowspan=4,sticky="NSEW")
        self.__buttons_student.grid(row=3,column=6)
        
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=4)
        self.columnconfigure(2,weight=2)
        self.columnconfigure(3,weight=2)
        self.columnconfigure(4,weight=1)
        self.columnconfigure(5,weight=2)
        self.columnconfigure(6,weight=2)
        self.rowconfigure(2,weight=1)

    def enable_buttons_on_finish(self,thread='main'):
        if thread == 'main':
            self.__main_thread_finished = True
        else:
            self.__student_thread_finished = True
        
        if self.__main_thread_finished and self.__student_thread_finished:
            
            self.__control_bar.enable()
            self.__radio_buttons.enable()
            
            self.__drawing_canvas_buttons.enable()
            # raise NotImplementedError
            self.__main_thread_finished = False
            self.__student_thread_finished = False

        

    def pause_callback(self):
        """
        PAUSE Thread Managements
        """
        if self.__current_thread :
            self.__current_thread.pause()
            self.__buttons.pause.config(state=DISABLED)
            self.__buttons.terminate.config(state=DISABLED)
            self.__buttons.resume.config(state=NORMAL)
    
    def resume_callback(self):
        """
        RESUME Thread Managements
        """
        if self.__current_thread :
            self.__current_thread.resume()
            self.__buttons.pause.config(state=NORMAL)
            self.__buttons.terminate.config(state=NORMAL)
            self.__buttons.resume.config(state=DISABLED)
    
    def terminate_callback(self):
        """
        STOP Thread Managements 
        """
        if self.__current_thread :
            self.__current_thread.stop()
            self.thread_finish()

    def delete_all(self):
        """
        TRASH Thread Managements
        """
        self.__on_element_release()
        self.__tree_canvas.canvas.delete("all")
        self.__buttons.delete.config(state=DISABLED)
        self.__T.config(state=NORMAL)
        self.__T.delete(0,"end")
        self.__T.insert(END, "Goal path will appear here")
        self.__T.config(state=DISABLED)
        self.__drawing_canvas.reset()
        # self.__control_bar.enable()
        # self.__radio_buttons.enable()
        # self.__drawing_canvas_buttons.enable()
        self.__initial_node.delete()
        self.__initial_node = None

        self.enable_buttons_on_finish()

    def thread_finish(self):
        """
        Clear current thread ptr(s)
        """
        self.__buttons.pause.config(state=DISABLED)
        self.__buttons.resume.config(state=DISABLED)
        self.__buttons.terminate.config(state=DISABLED)
        # print("Thread Finished")
        self.__buttons.delete.config(state=NORMAL)
        self.__current_thread = None
        
    def __goal_set(self,string):
        """
        GOAL node assignment
        """
        self.__T.config(state=NORMAL)
        self.__T.delete(0,"end")
        self.__T.insert(END, string)
        self.__T.config(state=DISABLED)
        self.thread_finish()
    
    def __goal_notfound(self):
        """
        GOAL NOT FOUND ENDING
        """
        self.__T.config(state=NORMAL)
        self.__T.delete(0,"end")
        self.__T.insert(END,"Goal was not found")
        self.__T.config(state=DISABLED)
        self.thread_finish()

    def pause_callback_student(self):
        """
        PAUSE Thread Managements
        """
        if self.__current_thread_student :
            self.__current_thread_student.pause()
            self.__buttons_student.pause.config(state=DISABLED)
            self.__buttons_student.terminate.config(state=DISABLED)
            self.__buttons_student.resume.config(state=NORMAL)
    
    def resume_callback_student(self):
        """
        RESUME Thread Managements
        """
        if self.__current_thread_student :
            self.__current_thread_student.resume()
            self.__buttons_student.pause.config(state=NORMAL)
            self.__buttons_student.terminate.config(state=NORMAL)
            self.__buttons_student.resume.config(state=DISABLED)

    def terminate_callback_student(self):
        """
        STOP Thread Managements 
        """
        if self.__current_thread_student :
            self.__current_thread_student.stop()
            self.thread_finish_student()

    def delete_all_student(self):
        """
        TRASH Thread Managements
        """
        self.__on_element_release()
        self.__tree_canvas_student.canvas.delete("all")
        self.__buttons_student.delete.config(state=DISABLED)
        self.__T_student.config(state=NORMAL)
        self.__T_student.delete(0,"end")
        self.__T_student.insert(END, "Goal path will appear here")
        self.__T_student.config(state=DISABLED)
        self.__drawing_canvas_student.reset()
        # self.__control_bar.enable()
        # self.__radio_buttons_student.enable()
        # self.__drawing_canvas_buttons.enable()
        self.__initial_node_student.delete()
        self.__initial_node_student = None

        self.enable_buttons_on_finish('student')





    def thread_finish_student(self):
        """
        Clear current thread ptr(s)
        """
        self.__buttons_student.pause.config(state=DISABLED)
        self.__buttons_student.resume.config(state=DISABLED)
        self.__buttons_student.terminate.config(state=DISABLED)
        self.__buttons_student.delete.config(state=NORMAL)
        self.__current_thread_student = None
    
    def __goal_set_student(self,string):
        """
        GOAL node assignment
        """
        self.__T_student.config(state=NORMAL)
        self.__T_student.delete(0,"end")
        self.__T_student.insert(END, string)
        self.__T_student.config(state=DISABLED)
        self.thread_finish_student()

    def __goal_notfound_student(self):
        """
        GOAL NOT FOUND ENDING
        """
        self.__T_student.config(state=NORMAL)
        self.__T_student.delete(0,"end")
        self.__T_student.insert(END,"Goal was not found")
        self.__T_student.config(state=DISABLED)
        self.thread_finish_student()


 

if __name__ == "__main__":
    """
    PROGRAM ENTRY POINT
    """
    root =  Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w = 2200 if w > 1200 else w
    h = 720 if h > 720 else h
    root.geometry("%dx%d+0+0" % (w, h))
    
    root.title('AI Graph Search')
    root.iconbitmap(os.path.join(BASE_DIR,'GUI','images','logo.ico'))
    can = MainCanvas(root,10,720)
    
    can.grid(row=0,column=0,sticky = "NSEW")
    
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    for arg in sys.argv:
        if arg[-5:] == '.gtxt':
          can.get_drawing_canvas().load(arg)  

    root.mainloop()
