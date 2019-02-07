class Node():
    def __init__(self, data):
        self.data = data
        self.nxt = None

class LinkedList:
    def __init__(self):
        self.head =  None

    def print_list(self):
       t = self.head
       while(t):
           print(t.data)
           t = t.nxt
    def push_first(self,data):
        new_head =  Node(data)
        new_head.nxt = self.head
        self.head = new_head
    
    def push_position_after(self,prev_node,data):
        if not isinstance(prev_node, Node): 
            print("Previous node must be in Linked List")
            return
        new_node = Node(data)
        # temp = prev_node.nxt 
        new_node.nxt = prev_node.nxt
        prev_node.nxt = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head =  new_node
            return
        
        last = self.head
        while(last.nxt):
            last = last.nxt
        last.nxt = new_node
# linked list
L =  LinkedList()
L.head =  Node(1)
second =  Node(2)
third  =  Node(3)
L.head.nxt = second
second.nxt =  third

data = 0
L.append(45)
L.push_first(0)
L.push_position_after(data,2.0)
L.print_list()