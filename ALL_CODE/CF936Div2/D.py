from collections import Counter
for _ in range(int(input())):
    
    n, m, x = map(int, input().split())
    s = set()
    for t in range(m):
        c, b = map(str, input().split())
        
        pos = (x+int(c)) if b=="0" else n-int(c) + x 
        if pos>n:
            pos = pos%n
        s.add(pos)
        x = pos
    s.add(x)

    print(len(s))
    print(*sorted(s))



        

        

    