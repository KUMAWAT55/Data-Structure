def balance_check(string):
    open_brackets=set('({[')
    pairs=set([('(',')'),('{','}'),('[',']')])
    Stack=[]
    if len(string)%2!=0:
        return False
    for paran in string:
        if paran in open_brackets:
            Stack.append(paran)
        else :
            if len(Stack)==0:
                return False
            last_open=Stack.pop()
            if (last_open,paran) not in pairs:
                return False
    return len(Stack)==0

if __name__=='__main__':
    print (balance_check('[{}]{}'))