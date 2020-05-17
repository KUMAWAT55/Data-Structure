def reverse(n):
    if len(n)==1:
        return n
    else:
        return n[len(n)-1]+reverse(n[:len(n)-1])
    #onemore
    #else
        #return reverse(n[1:])+n[0]

if __name__=='__main__':
    print (reverse('hello world'))