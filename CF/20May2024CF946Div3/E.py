for _ in range(int(input())):
    m, x = list(map(int, input().split()))
    c = [0]*m
    h = [0]*m
    for i in range(m):
        c[i], h[i] = map(int, input().split())
    dp = [float('-inf')] * (sum(h) + 1)
    ans = dp[0] = 0

    # print("c", c)
    # print("h", h)
    # print("dp", dp)
 
    for i in range(m):
        for j in range(len(dp)-1, -1, -1):
            if dp[j] + i*x >= c[i]:
                dp[j+h[i]] = max(dp[j+h[i]], dp[j] - c[i])
                ans = max(ans, j+h[i])
    print(ans)