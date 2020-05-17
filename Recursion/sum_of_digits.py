def rep_sum(n):
    if len(str(n))==1:
        return n
    else:
        return n%10+rep_sum(n//10)

if __name__=='__main__':
    print (rep_sum(10))