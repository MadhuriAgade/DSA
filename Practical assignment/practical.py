class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if self.front is None or new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next and temp.next.priority <= new_node.priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully")

    def display_next(self):
        if self.front is None:
            print("No patients waiting")
        else:
            print("Next Patient:")
            print("ID:", self.front.pid)
            print("Name:", self.front.name)
            print("Priority:", self.front.priority)

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Treated Patient:", temp.name)
            self.front = self.front.next

    def display_all(self):
        if self.front is None:
            print("No patients waiting")
        else:
            temp = self.front

            while temp:
                print(temp.pid, temp.name, temp.priority)
                temp = temp.next

q = PriorityQueue()

q.enqueue(Node(101, "Asha", 3))
q.enqueue(Node(102, "Rashi", 1))
q.enqueue(Node(103, "Meera", 2))
q.enqueue(Node(104, "Sahil", 1))

print("All Waiting Patients:\n")
q.display_all()

print("Next Patient:\n")
q.display_next()

print("After Treatment:\n")
q.dequeue()

print("Remaining Patients:\n")
q.display_all()