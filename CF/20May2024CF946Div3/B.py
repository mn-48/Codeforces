for _ in range(int(input())):
    n = int(input())
    s = list(input())
    a = sorted(set(s))
    b = a[::-1]

    dic = {}
    i = 0
    while i<len(a):
        dic[a[i]] = b[i]
        i+=1

    ans = ""
    for i in s:
        ans+=dic[i]
    print(ans)
    
    
    
   