# Function checks whether string1 and string2 are anagram of each other or not .
def anagram(string1,string2):
    s1=string1.replace(" ","").lower()
    s2=string2.replace(" ","").lower()
    if sorted(s1)==sorted(s2):
        return True
    return False

def anagram_approach2_efficient(string1,string2):
    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()
    count={}
    for letter in s1:
        if letter in count:
            count[letter]+=1
        else :
            count[letter]=1

    for letter in s2:
        if letter in count:
            count[letter]-=1
        else :
            count[letter]=1
    for k in count:
        if count[k]!=0:
            return False
    return True
if __name__ =='__main__':
    print(anagram_approach2_efficient('dog','god'))