for _ in range(int(input())):
    s = input()
    cnt = s.count('10')+ s.count('01')

    if "01" in s:
        cnt-=1
    print(cnt+1)