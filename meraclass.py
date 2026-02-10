import ctypes
class MeraList:
    def __init__(self):
     self.size=1
     self.n = 0
#we have to create a C type array with size= self.size
     self.A = self._make_array(self.size)

#Magic function
    def __len__(self):
       return self.n

    def _make_array(self,capacity):
       #create c type array (static,referential) with size capacity
       return(capacity*ctypes.py_object)()
    
    
   
    
L = MeraList()
print(type(L))
print(L)
print(L.n)
print(L.size)
len(L)

