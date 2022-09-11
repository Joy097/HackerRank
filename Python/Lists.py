if __name__ == '__main__':
    N = int(input())
    
    list=[]
    for i in range (N):
        g=input().split(' ')
        list.append(g)
    
   
    t=[]
    for i in range (N):
        if list[i][0]=='insert':
            t.insert(int(list[i][1]),int(list[i][2]))
        elif list[i][0]=='print':
            print(t)
        elif list[i][0]=='remove':
            t.remove(int(list[i][1]))
        elif list[i][0]=='append':
            t.append(int(list[i][1]))
        elif list[i][0]=='sort':
            k=sorted(t)
            t=k
        elif list[i][0]=='pop':
            t.pop()
        elif list[i][0]=='reverse':
            t.reverse()
    
            
    '''   
    Operations :
    
    insert()
    print()
    remove()
    append()
    sort()
    pop()
    reverse()
    '''
    
