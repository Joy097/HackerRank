if __name__ == '__main__':
    
    list=[]
    x=int(input())
    for i in range(x):
        g=[]
        name = input()
        score = float(input())
        g.append(name)
        g.append(score)
        list.append(g)
        
        
    for i in range(x):
        for j in range(i+1,x):
            if list[i][1]>list[j][1]:
                temp = list[i]
                list[i]=list[j]
                list[j]=temp
  
    
    
    for i in range(x):
        
        if list[0][1]<list[i][1]:
            
            q=list[i][1]
            break
        
        
   
    
    s=[]       
    for i in range(x):
        
        if list[i][1]==q:
            
            s.append(list[i][0])
            
    a=sorted(s)
    
    for i in a:
        print(i)
    