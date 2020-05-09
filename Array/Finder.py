def finder(arr1,arr2):
    for num1,num2 in zip(sorted(arr1),sorted(arr2)):
        if num1!=num2:
            return num1
if __name__ =='__main__':
    print (finder([5,7,6,3,4,1,2],[6,7,4,2,3,1]))
