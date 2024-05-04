for _ in range(int(input())):
    n= int(input())
    ans = 1
    if n%2==0:
        ans = 0

    print("YNEOS"[ans::2])
    if not ans:
        s = ""
        for i in range(0,n//2):
            s+=chr(65+i)+chr(65+i)
        print(s)

   
   
