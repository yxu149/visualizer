import settings.settings as settings 
import gui.wirings.element_ctrl as element_ctrl
import gui.modules.element as element 
import gui.modules.stage as stage 
import gui.utils.exceptions as exceptions
from abc import abstractmethod

class Node(element, element_ctrl): 
    def __init__(self, canvas, x, y, label, \
        heurastic=0, goal=False, initial=False, \
        expanded_level=1000000):
        super(Node, self).__init__(canvas) 
        self.adj = [] # carries adjancent nodes
        self.lines_out = [] # has all out lines 
        self.lines_in = [] # has all in lines
        self.__goal = goal # is this node a goal or not 
        self.__canvas = canvas # canvas object helps in drawing on screen
        self.__x = x # x coordinate of its center
        self.__y = y # y coordinate of its center
        self.__label = label # unique label used to identify each node used mainly in GUI 
        self.__initial = initial # boolean value to define if this node is initial or not
        self.__heurastic = heurastic
        self.visited = False
        self.__expanded_level = expanded_level
    
    def get_save_data(self):
        initial = '1' if self.__initial else '0'
        goal = '1' if self.__goal else '0'
        return str(self.__id) + '\t' + str(self.__label) + '\t' + str(self.__x) + '\t' + str(self.__y) + '\t' + str(self.__heurastic) + '\t' + initial + '\t' + goal +'\n'

    def set_heurastic(self,new_heurastic:int):
        if not self.__goal and  new_heurastic != self.__heurastic:
            self.__heurastic = new_heurastic
            self.__canvas.itemconfig(self.__heurastic_id, text=str(self.__heurastic))
    
    def get_heurastic(self):
        return self.__heurastic

    def get_label(self):
        return self.__label

    def set_label(self,new_label):
        if new_label != self.__label:
            self.__label = new_label
            self.__canvas.itemconfig(self.__label_id, text=str(new_label))


    def set_initial(self):

        self.__initial = True
        self.__reset_color()

    def reset_initial(self):
        
        self.__initial = False
        self.__reset_color()

    def set_goal(self):

        self.set_heurastic(0)        
        self.__goal = True
        self.__reset_color()

    def reset_goal(self):
        
        self.__goal = False
        self.__reset_color()

    def is_goal(self):
        
        return self.__goal

    def connect_node(self,node,weight=1):

        if node in self.adj :
            raise exceptions.DuplicateConnectionException()
            
        self.adj.append(node)
        l = line.Line(self.__canvas,self,node,weight)
        l.create()       
        self.lines_out.append(l)
        node.lines_in.append(l)
        return l

    def get_coor(self):
        return self.__x , self.__y

    def __create_circle(self): 
        
        x0 = self.__x - settings.NODE_RADIUS
        y0 = self.__y - settings.NODE_RADIUS
        x1 = self.__x + settings.NODE_RADIUS
        y1 = self.__y + settings.NODE_RADIUS
        overlap = self.__canvas.find_overlapping(x0, y0, x1, y1)
        if len(overlap):
            raise exceptions.OverlapException()
            
        return self.__canvas.create_oval(x0, y0, x1, y1,fill=settings.NODE_COLOR)


    def create(self):
        self.__id = self.__create_circle()
        self.__label_id = self.__canvas.create_text((self.__x, self.__y), text=self.__label)
        self.__heurastic_id = self.__canvas.create_text((self.__x-settings.NODE_RADIUS, self.__y-settings.NODE_RADIUS), text=self.__heurastic,fill=VALUE_COLOR)
        super(Node,self).set_id(self.__id)
        return self.__id

    def get_id(self):
        return self.__id
    
    def delete(self):
        
        for line in self.lines_in + self.lines_out:
            line.delete()
        
        self.__canvas.delete(self.__id)
        self.__canvas.delete(self.__label_id)
        self.__canvas.delete(self.__heurastic_id)
        del self

    def select(self):

        self.__canvas.itemconfig(self.__id, fill=CIRCLE_COLOR_SELECTED)

    def __reset_color(self):
        
        if self.__goal and self.__initial:
            self.__canvas.itemconfig(self.__id, fill=GOAL_INITIAL_COLOR)
        elif self.__initial:
            self.__canvas.itemconfig(self.__id, fill=INITIAL_NODE_COLOR)
        elif self.__goal:
            self.__canvas.itemconfig(self.__id, fill=GOAL_NODE_COLOR)
        else:
            self.__canvas.itemconfig(self.__id, fill=CIRCLE_COLOR_NORMAL)

    def deselect(self):
        
        self.__reset_color()
        

    def bind_event(self,callback,binded_event='<Button-1>'):
        self.__canvas.tag_bind(self.__id, binded_event, lambda event, arg=self.__id: callback(event, arg))
        self.__canvas.tag_bind(self.__label_id, binded_event, lambda event, arg=self.__id: callback(event, arg))

    def __str__(self):
    
        return "Node("+ str(self.__label)+")"

    def mark_visited(self):
        super().mark_visited()
        self.visited = True
    
    def reset(self):
        super().reset_cross()
        self.__reset_color()
        self.visited = False

    def set_expanded_level(self,level):
        self.__expanded_level = level if level < self.__expanded_level else self.__expanded_level

    def get_expanded_level(self):
        return self.__expanded_level
        
    def is_initial(self):
        return self.__initial

    def load(self,string:str):

        attr = string.split('\t')
        self.__label = attr[1]
        self.__x = float(attr[2])
        self.__y = float(attr[3])
        self.__heurastic = int(attr[4])
        self.__initial = (attr[5] == '1') 
        goal = (attr[6] =='1')
        self.create()
        if goal:
            self.set_goal()
        self.__reset_color()