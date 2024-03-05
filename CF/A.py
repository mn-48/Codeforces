from collections import deque
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(2*abs(a[-1]-a[0]+a[-2]-a[1]))
   
