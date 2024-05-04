from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # ans = 
    for key, ls in groupby(a):
        print(key, ls)
   