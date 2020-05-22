def minion_game(string):
    vowels=['A','E','I','O','U']
    Stuart_count=0
    Kevin_count=0
    length_s=len(string)
    for i in range(length_s):
       if string[i] in vowels:
            Kevin_count+=length_s-i
       else:
           Stuart_count+=length_s-i
    if Stuart_count>Kevin_count:
        print("Stuart "+str(Stuart_count))
    elif Kevin_count>Stuart_count:
        print("Kevin "+str(Kevin_count))
    else:
        print("Draw")

if __name__ == '__main__':
    minion_game('BANANA')