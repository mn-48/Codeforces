from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    # print(freq)
    ans = 0
    cnt = 0
    while freq[ans] > 1 or (freq[ans]==1 and cnt ==0 ):
        if freq[ans] == 1:
            cnt+=1
        ans+=1
    print(ans)
