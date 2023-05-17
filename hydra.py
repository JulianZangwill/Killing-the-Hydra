'''
Make a class Node() whose arguments are zero or more Nodes. Use it recursively to build a tree (=Hydra)
Print out its configuration and then call chop() on the root node. That will search for the first head, chop it off and make two copies as described in the video.
Repeat until nothing left.

t = Node(Node(Node(), Node(), Node()))
while not t.is_head():
    print(t)
    t.chop()


'''


class Node:
    def __init__(self, *args):
        self.children = []
        self.add(*args)
        self.parent = None

        self.level  = 0
        self.get_level()
        self.width = None
        self.get_width()
        

    def is_head(self):
        if self.children ==[]:
            return True

    def chop(self):
        child = self.children[0]
        if child.is_head():
            self.children.remove(child)
            if self.parent:
                for i in range(2):
                    self.parent.add(self.create_copy())
            print('Chopped')


        else:
            child.chop()

    def chop_myself(self):
        child = self
        if child.is_head():
            self.parent.children.remove(child)
            if self.parent.parent:
                for i in range(2):
                    self.parent.parent.add(self.parent.create_copy())
            else:
                pass
    
    def create_copy(self):
        node_list = [node.create_copy() for node in self.children]
        new_node = Node(*node_list)
        return new_node


    def add(self, *args):
        self.children.extend(list(args))
        for child in self.children:
            child.parent = self
    
    def __str__(self):
        
        if self.children == []:
            hydra = ' Head|'
        else:
            hydra = ' Node'
            add_ons = ''
            for child in self.children:
                add_ons = add_ons + str(child)

            #OR add_ons = ''.join(str(node) for node in self.nodes)

            hydra = hydra + '('+add_ons+')'
                

        return hydra


        ################################Plotting#####################################################
    def get_depth(self):
        depth = 0 if self.children == [] else max([1+child.get_depth() for child in self.children])
        return depth
    
    def get_level(self):
        for child in self.children:
            child.level = self.level + 1
    def get_width(self):
        self.width = len(self.children)

        



        


# t = Node(Node(Node()))
# while not t.is_head():
#     print(t)
#     t.chop()
# print('Hydra Defeated')