
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    yes = True
    
    first_max = []
    
    is_subset_method = set(b).issubset(set(a))
    if not is_subset_method:
        yes = False
        
    if yes:
        maxVal = a[0]
        for i in range(n):
            maxVal = max(maxVal, a[i])
            if b[i] > maxVal:
                yes = False
    
    
        
        
    print("YES" if yes==True else "NO") 
                
        