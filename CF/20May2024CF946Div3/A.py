import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    r1 = math.ceil(y/2)
    
    r2 = x- r1*7 if y%2==0 else x- r1*7-4
    if r2 > 0:
        r2 = math.ceil(r2/15)
    else:
        r2 = 0
    print(r1+r2)