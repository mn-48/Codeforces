for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    bmin = min(c,d)
    bmax = max(c,d)
    amin = min(a,b)
    amax = max(a,b)
    if bmin < amin: 
        amin, bmin =  bmin, amin
        amax, bmax =  bmax, amax
    ls = [i for i in range(amin,amax)] 
    if bmin in ls and bmax not in ls:
        print("Yes")
    else:
        print("NO")

    


   