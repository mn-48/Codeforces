# python A.py < test.in > test.out
import sys
R = lambda: map(int, next(sys.stdin).split())

n,= R()
*a, = R()

a = sorted(a, reverse=True)
A = 0
B = 0
for i in range(0, len(a)):

    if A>B:
        B+=a[i]
    else:
        A+=a[i]

print(A, B)