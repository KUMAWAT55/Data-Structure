#Stack Class
class Stack(object):
    def __init__(self):
        self.stack=[]
    def __len__(self):
        return len(self.stack)
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
    def peak(self):
        return self.stack[len(self.stack)-1]
    def show(self):
        return self.stack

if __name__=='__main__':
    stack=Stack()
    print(type(stack))
    stack.push(1)
    print(stack.show())
    stack.pop()
    print(stack.show())