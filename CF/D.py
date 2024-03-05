from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [-1] * n
    # print(ans)
    
    for i in range(n):
        # right site bigger
        right = i+1
        c = 0
        mnr = 0
        mnl = 0
        while  right<n and a[right] < a[i]:
            if a[right] > a[i]:
               mnr = c
               break
           
            c+= 1
            right += 1
        left = i-1
        c = 0
        while left>-1 and a[left] < a[i]:
            if a[left] > a[i]:
               mnl = c
               break
            c+= 1
            left -= 1
        ans[i] = min(mnr, mnl)
            
    print(ans)
             
        
    #     left = i-1
    #     
        
    #     mn = float("inf")
        
   

