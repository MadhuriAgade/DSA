
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        temp = self.top
        self.top = self.top.next
        return temp.data


class Lqueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Deleted:", temp.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def reverse(self):
        s = Stack()
        temp = self.front

        while temp:
            s.push(Node(temp.data))
            temp = temp.next

        self.front = self.rear = None

        while s.top:
            self.enqueue(Node(s.pop()))

    def merge(self, q1, q2):
        temp = q1.front
        while temp:
            self.enqueue(Node(temp.data))
            temp = temp.next

        temp = q2.front
        while temp:
            self.enqueue(Node(temp.data))
            temp = temp.next

    def identical(self, q1, q2):
        temp1 = q1.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                print("Queues are not identical")
                return
            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            print("Queues are identical")
        else:
            print("Queues are not identical")


q = Lqueue()

print("Enqueue:")
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.display()

print("\nDequeue:")
q.dequeue()
q.display()

print("\nReverse Queue:")
q.reverse()
q.display()

q1 = Lqueue()
q2 = Lqueue()

q1.enqueue(Node(10))
q1.enqueue(Node(20))

q2.enqueue(Node(10))
q2.enqueue(Node(20))

print("\nMerge Queues:")
q3 = Lqueue()
q3.merge(q1, q2)
q3.display()

print("\nCheck Identical:")
q3.identical(q1, q2)