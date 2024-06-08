from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()

    nai = []
    for i in "ABCDEFG":
        if i not in s:
            nai.append(i)

    ans = m*len(nai)

    cnt = Counter(s)
    # print(cnt)

    for x in cnt:
        # print(x, cnt.get(x))
        p = cnt.get(x)
        if p < m:
            ans += m-p
    print(ans)