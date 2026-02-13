# Task1 to create list which behave as a dynamic array
import ctypes
class MeraList:
    def __init__(self):
        self.size=1
        self.n=0
        #create a c type array with size =self.size
        self.A= self. _make_array(self.size)

    def _make_array(self,capacity):
        return(capacity*ctypes.py_object)()
    
   #  Custom function for length
    def __len__(self):
     return self.n
    
   #cust

    
L=MeraList()
print(L)  
print(L.size)
print(L.n)
     
print(type(L))
print(len(L))
