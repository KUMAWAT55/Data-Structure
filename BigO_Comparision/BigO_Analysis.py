#This function is sample example to define the BigO notation and how to calculate .
import time
def comp(lst):
    start_time=time.time()
    print (lst[0])
    #Complexity of above expression is constant O(1) .
    #######################
    midpoint=len(lst)//2
    for i in lst[:midpoint]:
        print(i)
    ##Complexity of above expression is constant O(n/2) .
    ##################
    for x in range(10):
        print ("Hello")
    end_time=time.time()
    return start_time-end_time
    ##Complexity of above expression is constant O(10) .


if __name__=='__main__':
    lst=[1,2,3,4,5]
    print(comp(lst))
    #TOTAL Complexity = O(1)+O(n/2)+O(10)
    #O(n/2) will increase with increase in size of n , while other O(1) and O(10)  can be neglected at large scale .
    #TOTAL = O(n/2)
     