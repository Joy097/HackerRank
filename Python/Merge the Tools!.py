import textwrap
def merge_the_tools(string, k):
    # your code goes here
    x=textwrap.wrap(string,k)
    '''
    s=[]
    a=0
    for i in range (len(string)):
        
        if a==k :
            s.append()
        a+=1
        '''
    
    
            
    def One_alphabet(s): 
        w=[]
        for i in range(len(s)):
            w.append(s[i])
               
        i=0        
        while i<(len(w)):
            for j in range(i+1,len(w)):
                if w[i] == w[j]:
                    w.pop(j)
                    i-=1
                    break
            i+=1
        q=''
        for i in range(len(w)):
            q+=w[i]
        return q
    a=[]
    for i in range (len(x)):
        
        a.append(One_alphabet(x[i]))
    
        
    for i in range (len(a)):
        print (a[i])
        
    