for _ in range(int(input())):
    n = int(input())
    s = input()
    r = sum(x=="1" for x in s)
    l = 0

    u = []
    for i in range(n+1):
        if l*2 >= i and r*2 >= n-i:
            u.append(i)
        if i == n:
            break
        r -= "1" == s[i]
        l += "0" == s[i]
    u.sort(key=lambda x: abs(n-x*2))
    print(u[0])