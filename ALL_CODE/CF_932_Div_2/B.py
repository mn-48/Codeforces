# python A.py < test.in > test.out
import sys
R = lambda: map(int, next(sys.stdin).split())
t,=R()
while t:
    t-=1
    n,x= R()
    *a, = R()
ans = 0
print(ans)