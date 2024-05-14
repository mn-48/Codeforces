def solve(x):
    res = x-1
    j = x-1
    for i in range(1, x):
        while i*i + j*j >= x*x:
            j-=1
        res+=j
    return res*4+1
    
for _ in range(int(input())):
    r = int(input())
    print(solve(r+1)-solve(r))

   