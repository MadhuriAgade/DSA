#Linear queue using linked list
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
    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next        