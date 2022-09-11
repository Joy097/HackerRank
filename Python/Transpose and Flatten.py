# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

ra=input().split(' ')

list=[]
for i in range (int(ra[0])):
    
    col=input().split(' ')
    list.append(col)
    
arr=numpy.array(list,int)



print (numpy.transpose(arr))

print(arr.flatten())

    
        
        
        
