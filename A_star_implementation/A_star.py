import pygame as pg
from queue import PriorityQueue
import math

# The size of the grid
width = 800
window = pg.display.set_mode((width , width))
pg.display.set_caption('A-star path finder')


# Some color codes for the future use
red = (255,0,0)  # color for the visited nodes
white = (255,255,255) # Color for the non-visited nodes
green = (0,255,0)
golden = (255,215,0) # Color of the start-Node
blue = (0,0,255)
yellow = (255,255,0)
purple = (130,0,130)  # Color of the shortest path between the start and the end nodes
grey = (129,129,129)
black = (0,0,0)   # Barrier or Walls of the maze
Turquoise = (64,224,208)

# Creating the node class
class Node:
    def __init__(self , rows , cols , width , rows_total):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.rows_total = rows_total
        self.color = white
        self.x_axis = rows * width
        self.y_axis = cols * width

    # Following are the methods for certain checks on Nodes!!!!

    # To get the position (R x C) type
    def get_position(self):
        return self.rows , self.cols

    # To check whether the node has been visited
    # If the node is of color 'white' it means it's not visited yet ...
    # If it's 'red' it is...
    def check_node(self):
        return self.color == red

    # To check the barrier or obstacle
    def check_bars(self):
        return self.color == black

    # Start node color
    def start_node(self):
        return self.color == golden

    # End node
    def end_node(self):
        return self.color == blue


    # To reset the grid to all white
    def reset_grid(self):
        self.color = white

    # prio-queue
    def is_open(self):
        return self.color == green

    # To actually do the stuff we will use the following methods

    def make_node(self):
        self.color = red

    def make_open(self):
        self.color = green


    def make_bars(self):
        self.color = black

    def make_end_node(self):
        self.color = blue

    def make_path(self):
        self.color = purple



    # To draw a cube
    def draw_cube(self , window):
        pg.draw.rect(window , self.color , (self.x_axis , self.y_axis , self.width , self.width))

    def update_neighbr_nodes(self):
        pass

    def __lt__(self, other):
        return False




# To make the Heuristic-Function between two nodes n1 and n2 for e.g
def heuristic(n1 , n2):
    x1 , y1 = n1
    x2 , y2 = n2
    return abs(x2-x1) + abs(y2-y1)


def make_the_grid(rows , width):
    grid_ls = []
    cube_gap = width // rows
    for i in range(rows):
        grid_ls.append([]) #make a 2D list like [[] , [] , []
                                                #[] , [] , [] ]
        for j in range(rows):
            node = Node(i , j , cube_gap , rows)    # ==> object of the Node class: Node(i = rows , j = cols , cube_gap = width , rows = rows_total)
            grid_ls[i].append(node)  # Passed the object of the class into the list or Grid on the ith row!!

    return grid_ls

# To draw a line to separate the rows and column to give it a look like in all board games!!!
def make_grid_lines(window , rows , width):
    cube_gap = width // rows

    # for horizontal lines
    for i in range(rows):
        pg.draw.line(window , grey , (0,i*cube_gap) , (width , i*cube_gap))   # x-axis = (0,i*cube_gap) , y-axis =(width,i*cube_gap)  : when i =0 , 0*0 will be(0,0) so the first line will be at 0,0 and so on...
        # for vertical lines
        for j in range(rows):
            pg.draw.line(window , grey , (j*cube_gap , 0) ,(i*cube_gap , width) )


def draw(window , grid_ls , rows , width):
    window.fill(white)  # fill the screen with white color

    # Draw all the Grids
    for row in grid_ls:
        for node in rows:
            node.draw(window)

    # Now we will draw some grid line on top with the make_grid_lines  function
    make_grid_lines(window , rows , width)

    # Take what-ever we have drawn and update the Grid accordingly
    pg.display.update()
