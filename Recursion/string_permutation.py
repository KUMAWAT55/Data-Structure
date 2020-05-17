def permute(string):
    out=[]
    if len(string)==1:
        return [string]
    for index,letter in enumerate(string) :
        for perm in permute(string[:index]+string[index+1:]):
            out+=[letter+perm]
    return out



if __name__ == '__main__':
    print(permute('ab'))
    print(permute('abc'))
    print (permute('abcd'))