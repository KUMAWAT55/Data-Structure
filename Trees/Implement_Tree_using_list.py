def Tree(Value):
    return [Value,[],[]]

def insertLeft(root,leftVal):
    t=root.pop(1)
    if len(t)>1:
        return root.insert(1,[leftVal,t,[]])
    else:
        root.insert(1,[leftVal,[],[]])
    return root

def insertRight(root,rightVal):
    t=root.pop(2)
    if len(t)>1:
        return root.insert(2,[rightVal,[],t])
    else:
        root.insert(2,[rightVal,[],[]])
    return root
def getRoot(root):
    return root[0]

def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]





if __name__ == '__main__':
    BT=Tree(10)
    print(BT)
    insertLeft(BT,8)
    print(BT)
    insertRight(BT, 9)
    print(BT)
    print(getRoot(BT))
    print(getLeftChild(BT))
    print(getLeftChild(BT))