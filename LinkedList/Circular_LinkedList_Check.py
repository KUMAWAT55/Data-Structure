class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None


def cycle_check(node):
    marker1=node
    marker2=node
    while marker1.nextnode!=None and marker2.nextnode!=None:
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode
        if marker1==marker2:
            return True
    return False
if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.nextnode=b
    b.nextnode=c
    c.nextnode=a
    #Cycle Here
    print(cycle_check(a))
    #Removed Cycle
    c.nextnode=None
    print(cycle_check(a))
