def compress(string):
    co_string=''
    l=len(string)
    cnt=1
    if l==1:
        return string+str(cnt)
    i=1
    while i < l :
        if string[i]==string[i-1]:
            cnt+=1
        else:
            co_string=co_string+string[i-1]+str(cnt)
            cnt=1
        i+=1
    co_string = co_string + string[i - 1] + str(cnt)
    return co_string

if __name__=='__main__':
    print(compress('AABBBBBBBCCR'))