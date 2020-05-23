def no_idea(n,m,array,A,B):
        return [(i in A)-(i in B) for i in array]


if __name__=='__main__':
    n,m=map(int,input().split(' '))
    array=list(map(int,input().split(' ')))
    A=list(map(int,input().split(' ')))
    B=list(map(int,input().split(' ')))
    print(no_idea(n,m,array,A,B))
