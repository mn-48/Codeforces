for _ in range(int(input())):
    n = int(input())
    ls = []
    for i in range(n):
        s = input()
        one_count = s.count('1')
        if one_count > 0:
            ls.append(one_count)

    print("SQUARE" if ls[0]==ls[1] else "TRIANGLE")

    

    

   

    