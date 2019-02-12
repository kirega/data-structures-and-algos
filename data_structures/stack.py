"""
    Stack implemtation in OOP
"""
from sys import maxsize

class Stack():
    def __init__(self):
        self.stack = []
        
    def isEmpty(self): 
        return len(self.stack) == 0

    def pop(self): 
        if (self.isEmpty()): 
            return str(-maxsize -1) #return minus infinite       
        return self.stack.pop() 

    # Function to add an item to stack. It increases size by 1 
    def push(self, item): 
        self.stack.append(item) 
        print("%s pushed to stack"%(item)) 
    
    def peek(self): 
        if self.isEmpty(): 
            return float("-inf") 
        return self.stack 
stack = Stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 
stack.pop()
print(stack.peek())
