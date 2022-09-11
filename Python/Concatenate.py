# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

ra=input().split(' ')

list1=[]
for i in range (int(ra[0])):
    
    col=input().split(' ')
    list1.append(col)
    
list2=[]
for i in range (int(ra[1])):
    
    col=input().split(' ')
    list2.append(col)
    

arr=numpy.array(list1,int)
arr1=numpy.array(list2,int)

print(numpy.concatenate((arr,arr1),axis=0))
