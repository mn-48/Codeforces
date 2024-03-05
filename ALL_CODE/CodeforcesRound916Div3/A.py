for _ in range(int(input())):
    n = int(input())
    s = input()
    set_s = set(s)
    cnt = 0
    for i in set_s:
        if s.count(i) >= ord(i)-64:
            cnt+=1
    print(cnt)
   
        
 
    

    
        
        
        
        
    
  
                
        
            
        
    
        
        
        
    
    # cnt = 0
    
    # for i in range(range(len(s))):
    #     if _log[s[i]]==i+1:
    #         cnt+=1
    # print(cnt)
   
        
    
    
    
    
        