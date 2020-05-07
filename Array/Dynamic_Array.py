import sys
data=[]
n=10
for i in range(n):
    a=len(data)
    b=sys.getsizeof(data)
    data.append(i)
    print ("Element : {0:3d} and Size : {1:1d}".format(a,b))
    #This program states how dynamic array increase extra space as the number of elements gets append .