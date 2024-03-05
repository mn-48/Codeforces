# t=int(input())
# while t:
# 	t-=1
# 	h,w,a,b,c,d=map(int,input().split())
# 	#print("-------------")
# 	al=c-a-1
 
# 	if a>=c:
# 		print("Draw")
# 		continue
# 	if al%2==0:
# 		n=al/2
# 		d1=min(d+n,w)
# 		d2=max(d-n,1)
# 		b1=min(b+n+1,w)
# 		b2=max(b-n-1,1)
# 	#	print(d1,d2,b1,b2,n)
# 		if d1<=b1 and  d2>=b2:
# 			print("Alice")
# 		else:
# 			print("Draw")
# 	else:
# 		n=al+1
# 		n/=2
# 		d1=min(d+n,w)
# 		d2=max(d-n,1)
# 		b1=min(b+n,w)
# 		b2=max(b-n,1)
# 	#	print(d1,d2,b1,b2)
# 		if d1>=b1 and  d2<=b2:
# 			print("Bob")
# 		else:
# 			print("Draw")

for _ in range(int(input())):
    h, w, a, b, c, d = map(int, input().split())
    al = c-a-1
    if a>=c:
        print("Draw")
        continue
    if al%2==0:
        n= al//2
        d1 = min(d+n, w)
        d2 = max(d-n, 1)
        b1 = min(b+n+1, w)
        b2 = max(b-n-1, 1)
        if d1<=b1 and d2>=b2:
            print("Alice")
        else:
            print("Draw")
    else:
        n= (al+1)//2
        d1 = min(d+n, w)
        d2 = max(d-n, 1)
        b1 = min(b+n, w)
        b2 = max(b-n, 1)
        if d1>=b1 and  d2<=b2:
            print("Bob")
        else:
            print("Draw")


