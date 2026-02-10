# Techniques to measure time efficiency of an program
import time
start=time.time()
for i in range(1,101):
    print(i) 
# i=1
# while(i<101):
#     print(i)
#     i+=1 
print(time.time()-start)    


L=[1,2,4,5,6]
for i in L:
    for j in L:
        print('({},{})'.format(i,j))

# Program to convert integer into string
def intToSTR(i):
    digits='0123456789'
    if i==0:
        return '0'
    result=''
    while i>0:
        result= digits[i%10] + result
        i=i//10
    
    return result
num=int(input("enter the ineteger number"))
string_value=str(intToSTR(num))
print(f"String value:'{string_value}'")


