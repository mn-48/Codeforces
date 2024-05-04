p = int(1e9+7) 
for _ in range(int(input())):
    n, k = map(int, input().split())
    a  = list(map(int, input().split()))
    
    mn, mx, sm = 0, 0, 0
    
    for i in a:
        sm += i
        mn = min(mn, sm)
        mx = max(mx, sm-mn)
        
    sm -= mx
    mx += mx * (1<<k) - mx
    print((sm+mx)%p)
    
        
    
    