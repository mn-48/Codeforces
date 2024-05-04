import math
for _ in range(int(input())):
    x = int(input())
    ans = x-1
    for y in (1,x):
        if x == math.gcd(x,y)+y:
            ans = y
            break
    print(ans)
    
    