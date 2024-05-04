for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    fail = False
    p = 0
    for x in a:
        if x>=10 and x//10 >= p and x%10 >= x//10:
            p = x%10
        else:
            if x>= p:
                p=x
            else:
                fail = True
                break
    print("YNEOS"[fail::2])
        

 
    
    

