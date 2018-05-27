class stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[len(self.stack)-1]
    
    def push(self,new_value):
        self.stack.append(new_value)

    def pop(self):
        last_element = self.stack[len(self.stack)-1]
        self.stack = self.stack[:len(self.stack)-1]
        return last_element
