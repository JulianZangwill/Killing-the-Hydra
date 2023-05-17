from hydra import Node

t = Node(Node(Node()))
while not t.is_head():
    print(t)
    t.chop()
print('Hydra Defeated')