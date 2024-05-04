from collections import deque
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    alice  = a[::2]

    mex = max(alice)+1

    alice = set(alice)
    for i in range(mex):
        if i not in alice:
            mex = i
            break
    print(mex)


    
    