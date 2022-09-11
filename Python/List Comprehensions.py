if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l=[]
    x+=1
    y+=1
    z+=1


    for i in range (0,x):           #0-2
        for j in range (0,y):       #0-3
            for b in range (0,z):
                
                c=i+j+b
                
                if c!= n:    
                    h=[]                #0-4
                    h.append(i)
                    h.append(j)
                    h.append(b)
                    l.append(h)
    print(l)
    
    
