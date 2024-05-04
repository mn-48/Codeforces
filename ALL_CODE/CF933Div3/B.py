for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n-2):
        x = max(0, a[i])
        a[i] -= x
        a[i+1] -= 2*x
        a[i+2] -= x
    print("YNEOS"[any(a)::2])
    

