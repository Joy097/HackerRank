r=int(input())
line=input().split(' ')

for i in  range(r) :
    line[i]=int(line[i])

for i in range (r): 
    for j in range(i+1,r):
        if line[i]<line[j]:
            temp=line[i]
            line[i]=line[j]
            line[j]=temp

#print(line)

for i in range (r):
    if line[i]!=line[i+1]:
        print(line[i+1])
        break

