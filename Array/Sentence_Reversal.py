def reverse(sentence):
    space=[' ']
    words_list=[]
    length=len(sentence)
    i=0
    while i < length :
        if sentence[i] not in space:
            words_start=i
            while i < length and sentence[i] not in space:
                i+=1
            words_list.append(sentence[words_start:i])
        i+=1
    return list(reversed(words_list))

if __name__=='__main__':
    print(reverse('    Hello World'))

