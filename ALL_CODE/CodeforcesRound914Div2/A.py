for _ in range(int(input())):
    ab = input()
    
    a = int(ab[0])
    cnt = 1 if ab[0]!='0' else 0
    while ab[cnt]=='0':
        if cnt >= len(ab)-1:
            break
        cnt+=1
        
        # print("cnt: ", cnt)
    
    if cnt<len(ab):
        a = int(ab[:cnt])
        b = int(ab[cnt:])
        # print(a,b)
        if a<b:
            print(a,b)
        else:
            print(-1)
    else:
        print(-1)
        