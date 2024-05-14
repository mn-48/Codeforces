for _ in range(int(input())):
    s = input()

    if len(set(s)) < 2:
        print("NO")
    else:
        print("YES")
        s1 = s[0]
        
        for i in range(1,len(s)):
            if s[i] != s1:
                print(s[i:]+s[0:i])
                break


