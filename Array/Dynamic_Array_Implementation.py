#This implementation is to know , How Dynamic array class works in python .
import ctypes
class dynamic_array(object):
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)

    def __len__(self):
        return self.n
    def __getitem__(self, index):
        if not 0<= index < self.n:
            return IndexError("Index out of bound Exception")
        return self.A[index]
    def append(self,element):
        if self.n==self.capacity:
            self.__resize(2*self.capacity)
        self.A[self.n]=element
        self.n+=1
    def _resize(self,new_cap):
        B=self.make_array(new_cap)
        for k  in range(self.n):
            B[k]=self.A[k]
        self.A=B
        self.capacity=new_cap
    def make_array(self,new_cap):
        return (new_cap*ctypes.py_object)()



if  __name__=='__main__':
    arr=dynamic_array()
    arr.append(1)
    print(arr[1])