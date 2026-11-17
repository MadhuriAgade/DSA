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
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next

    def display(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse_string(self, string):
        s = Stack()
        for ch in string:
            s.push(Node(ch))

        while s.top:
            print(s.top.data, end="")
            s.top = s.top.next
        print()

    def reverse_stack(self):
        s = Stack()
        while self.top:
            temp = self.top
            s.push(Node(temp.data))
            self.top = self.top.next
        self.top = s.top


st = Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))

print("Stack:")
st.display()

st.pop()

print("Reversed String:")
st.reverse_string("PYTHON")

st.reverse_stack()
print("Reversed Stack:")
st.display()