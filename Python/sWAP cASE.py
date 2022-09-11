def swap_case(s):
    a=''
    
    for i in range(len(s)):
        
        q=int(ord(s[i]))
        
        e=s[i]
        
        
        
        if q>64 and q<91 :
            a+=e.lower()
            #print(e.lower())
            
        elif q>96 and q<123 :
            a+=e.upper()
            
            
        
        else:
            a+=e
           
        
    
    
    return a

