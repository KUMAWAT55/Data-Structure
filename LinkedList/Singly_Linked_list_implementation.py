#Singly Linked List
class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None

if __name__ == '__main__':
    a= Node(1)
    b= Node(2)
    a.nextnode=b
    print(a)
    print(a.value)
    print(a.nextnode)
    print(a.nextnode.value)
    print (b)
    print(b.value)
    print(b.nextnode)