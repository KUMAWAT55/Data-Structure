#Deque Class
class Deque(object):
    def __init__(self):
        self.deque=[]
    def __len__(self):
        return len(self.deque)
    def addFront(self,item):
        self.deque.append(item)
    def deleteFront(self):
        self.deque.pop()
    def addRear(self,item):
        self.deque.insert(0,item)
    def deleteRear(self):
        self.deque.pop(0)
    def show(self):
        return self.deque

if __name__=='__main__':
    deque=Deque()
    print(type(deque))
    deque.addFront(1)
    print(deque.show())
    deque.addRear(2)
    print(deque.show())
    deque.deleteRear()
    print(deque.show())
