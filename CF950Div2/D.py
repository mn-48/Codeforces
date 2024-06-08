from math import gcd
 
def check_gcd(a):
	prev = gcd(a[0], a[1])
	for i in range(1, len(a) - 1):
		new = gcd(a[i], a[i + 1])
		if prev <= new:
			prev = new
		else:
			return i
 
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
 
	p = check_gcd(a)
	if p == None:
		print("YES")
	else:
		for i in range(max(0, p - 2), min(n, p + 2)):
			p = check_gcd(a[:i] + a[i + 1:])
			if p == None:
				break
		if p == None:
			print("YES")
		else:
			print("NO")