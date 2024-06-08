for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = "NO"
    if x>=y and (x-y)%2==0:
        ans="YES"
    print(ans)


        