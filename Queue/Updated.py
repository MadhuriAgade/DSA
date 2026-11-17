#
class Node:
    def __init_(self,value):
        self.data = value
        self.next = None
class Lqueue:
    def __init(self):
        self.front = self.rear = None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear=new_node
        else:
            self.front=self.rear = new_node                
    def dequeue(self):
        temp = self.front
        print("deleted node: ",temp.data)
        self.front= self.front.next
        if self.front == None:
            print("QAueue is empty now")
            self.rear = None
        temp = None
    def print(self):
        temp = self.front    
        while temp:
            print(temp.data, end="->")
            temp = temp.next        

que = Lqueue()
que.enqueue(Node(12))            
que.enqueue(Node(13))            
que.enqueue(Node(14))            
que.enqueue(Node(15))            
que.print()
que.dequeue()
que.dequeue()
que.dequeue()