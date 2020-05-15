# def solver(array):
#     ini_array=sorted(array)
#     for element in ini_array:
#         if ini_array.index(element)-array.index(element)>2:
#             return 'Too chaotic'
#     for element in array:

def solver(array):
    count=0
    array_check=[P-1 for P in array]
    for i,P in enumerate(array_check):
        print("i:",i,"P:",P)
        if P-i >2:
            return 'Too chaotic'
        for j in range(max(P-1,0),i):
            print("j:", j, "max:", max(P-1,0),"arrray--j:",array_check[j],"P:",P)
            if array_check[j]>P:
                print("True")
                count+=1

    return count



if __name__=='__main__':
    no_0f_cases=int(input())
    for i in range(no_0f_cases):
        l=int(input())
        array=[int(i) for i in input().split(' ')]
        print(solver(array))
