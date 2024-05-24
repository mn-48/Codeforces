for s in [*open(0)][2::2]:
    a = {}
    b = {}
    i = j = l = 0
    for x in s.split():
        a.setdefault(x := int(x), i)
        r = b[x] = i
        i += 1
    while j in a and (l := max(l, a[j])) < (r := min(r, b[j])):
        j += 1
    print(*([-1], (2, 1, r, r+1, i))[l < r])

    
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

#     cnt = 0
#     for i in sorted(a):
#         if i==cnt:
#             cnt+=1
#     s = set(range(cnt))

#     for i in range(n):
#         if a[i] in s:
#             s.remove(a[i])
#         if len(s) == 0:
#             if len(set(range(cnt))- set(a[i+1:])) == 0:
#                 print(2)
#                 print(f"{1} {i+1}\n{i+2} {n}")
#                 break
#     else: print(-1)
