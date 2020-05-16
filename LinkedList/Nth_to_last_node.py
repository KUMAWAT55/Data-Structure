class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None

def nth_to_last_node(n,node):
    rightptr=node
    leftptr=node
    for i in range(n-1):
        if not rightptr.nextNode:
            raise LookupError("Error not enough nodes")
        rightptr=rightptr.nextNode
    while rightptr.nextNode:
        rightptr=rightptr.nextNode
        leftptr=leftptr.nextNode
    return leftptr.value


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.nextNode=b
    b.nextNode=c
    c.nextNode=d
    print(nth_to_last_node(5,a))

