def merge_the_tools(string, k):
    from collections import OrderedDict
    lens=len(string)
    for i in range(0,lens+1,k):
        word=''.join(OrderedDict.fromkeys(string[i:i+k]).keys())
        print(word)

if __name__ == '__main__':
    merge_the_tools('AABCAAADA',3)