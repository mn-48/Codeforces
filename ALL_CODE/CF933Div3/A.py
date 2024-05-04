for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0 
    for i in a:
        for j in b:
            if i+j <=k:
                cnt +=1 
    print(cnt)

   
   
