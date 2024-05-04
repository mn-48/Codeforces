import sys
R = lambda: map(int, next(sys.stdin).split())
t,=R()

while t:
    t-=1
    n, = R()
    s = input()
    s1 = s[::-1]
    print(s if s<=s1 else s1+s)

