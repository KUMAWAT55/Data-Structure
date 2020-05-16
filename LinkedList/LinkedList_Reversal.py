class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None


def reverse(headNode):
    current=headNode
    previous=None
    nextnode=None
    while current:
        nextnode=current.nextNode
        current.nextNode=previous
        previous=current
        current=nextnode
    return previous






if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.nextNode=b
    b.nextNode=c
    c.nextNode=d
    print(a.nextNode.value)
    print(b.nextNode.value)
    print(c.nextNode.value)
    print(d.nextNode)
    reverse(a)
    print(a.nextNode)
    print(b.nextNode.value)
    print(c.nextNode.value)
    print(d.nextNode.value)
