#Singly Linked List
class DLNode(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        self.prevnode=None

if __name__ == '__main__':
    a= DLNode(1)
    b = DLNode(2)
    c=DLNode(3)
    a.nextnode=b
    b.prevnode=a
    b.nextnode=c
    c.prevnode=b
    print(a.value)
    print(a.prevnode)
    print(a.nextnode.value)
    print(b.value)
    print(b.prevnode.value)
    print(b.nextnode.value)
    print(c.value)
    print(c.prevnode.value)
    print(c.nextnode)
