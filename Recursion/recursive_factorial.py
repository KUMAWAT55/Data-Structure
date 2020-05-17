def rec_sum(n):
    if n==1 or n==0:
        return 1
    else:
        return n*rec_sum(n-1)

if __name__=='__main__':
    print (rec_sum(0))