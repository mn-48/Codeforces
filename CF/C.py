for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    
    counter = 1
    
    for i in range(1, n):
        if s1[i] == s2[i-1]:
            counter +=1
        elif s1[i] < s2[i-1]:
            counter = 1
        else:
            i = i-1
            break
    print(s1[:1+1]+s2[i:])
        