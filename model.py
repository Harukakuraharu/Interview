class Stack():

    def __init__(self)-> None:
        self.stack = []
    
    def is_empty(self) -> bool:
        return True if not self.stack else False
    
    def push(self, element)-> None:
        self.stack.append(element)

    def pop(self) -> list:
        del_element = self.stack.pop()
        return del_element
    
    def peek(self) -> list:
        return self.stack[-1]
    
    def size(self) -> int:
        return len(self.stack)

