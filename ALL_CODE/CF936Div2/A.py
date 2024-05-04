
import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    m = math.ceil(n/2)
    
    cnt = a[m-1:].count(a[m-1])
    
    print(cnt)
    
    