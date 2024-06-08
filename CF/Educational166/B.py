for _ in range(int(input())):
    n = int(input())
    ans = []
    while n:
        if n%2 ==0:
            ans.append(0)
        else:
            if n%4==1:
                ans.append(1)
            else:
                ans.append(-1)
                n+=1
        n = n//2
    print(len(ans))
    print(*ans)
    
