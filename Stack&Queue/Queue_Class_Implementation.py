#Queue Class
class Queue(object):
    def __init__(self):
        self.queue=[]
    def __len__(self):
        return len(self.queue)
    def enqueue(self,item):
        self.queue.insert(0,item)
    def dequeue(self):
        self.queue.pop()
    def show(self):
        return self.queue

if __name__=='__main__':
    queue=Queue()
    print(type(queue))
    queue.enqueue(1)
    print(queue.show())
    queue.enqueue(2)
    print(queue.show())
    queue.dequeue()
    print(queue.show())