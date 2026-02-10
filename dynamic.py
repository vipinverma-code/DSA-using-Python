import sys
L=[]
# L = []
# size=sys.getsizeof(L)
# print(size)
# L.append('hello')
# new_size=sys.getsizeof(L)
# print(new_size)

for i in range(100):
    print(i,sys.getsizeof(L))
    L.append(i)