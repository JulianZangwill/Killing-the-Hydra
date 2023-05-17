from plot import Plot
from hydra import Node

global monster
monster = Node(Node(Node(), Node()), Node(Node(), Node(Node())))

node_coordinates = []

r = 10


def plot_nodes(node, x0,y0, height, width):
    #initially plots circle

    #number of child heads
    child_number = len(node.children)

    if child_number == 0:
        plot.circle(x0, y0, r,'blue')
        node_coordinates.append([node, x0,y0])
        spacing = 0

    else:
        plot.circle(x0,y0, r,'brown')
        node_coordinates.append([node,x0,y0])
        spacing = width/(child_number+1)
 

    
    x_shift = width/2
    new_y = y0 + height

    for count, child in enumerate(node.children):
        if child_number!=1:
             new_x = x0 - x_shift + spacing*(count+1)
        else:
             new_x = x0
        
        plot.line(x0, y0, new_x, new_y)
        
        child_children = child.children
        if child.children != []:
            new_width = width/(child_number)
        else:
            new_width = width

        plot_nodes(child,new_x, new_y,height, new_width)

def resizing_function():
    refresh()



def motion_function(x,y):
    for node, x_c, y_c in node_coordinates:
        if (abs(x-x_c)< r and abs(y-y_c)< r):
            #print('Node')
            pass

def click_function(x,y):
    for node, x_c, y_c in node_coordinates:
        if (abs(x - x_c)< r and abs(y - y_c)< r):
            print('Clicked Node')
            clicked_node = node
            clicked_node.chop_myself()
            break
            
    refresh()
            
def refresh():
    plot.clear()
    node_coordinates.clear()

    depth = monster.get_depth()
    if depth == 0:
        print('Hydra Dead')
    height = (plot.height-20)/(depth+1)
    width = plot.width


    x0 = plot.width/2
    y0 = 20
    plot_nodes(monster, x0, y0, height, width)

plot = Plot(click = click_function, motion = motion_function, resize = resizing_function )

plot.loop()