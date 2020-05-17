def rec_sum(n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        return n+rec_sum(n-1)

if __name__=='__main__':
    print (rec_sum(4))